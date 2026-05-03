from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Order, OrderItem
from products.models import Product
from stores.models import Store
import json

@login_required
def checkout_view(request):
    if request.method == 'POST':
        cart_data = request.POST.get('cart_data')
        if not cart_data:
            messages.error(request, "Your cart is empty.")
            return redirect('product_list')
        
        try:
            cart = json.loads(cart_data)
            if not cart:
                messages.error(request, "Your cart is empty.")
                return redirect('product_list')
            
            # Group items by store (since an Order in our model is per store)
            store_items = {}
            for item in cart:
                product = get_object_or_404(Product, id=item['id'])
                store_id = product.store.id
                if store_id not in store_items:
                    store_items[store_id] = []
                store_items[store_id].append({
                    'product': product,
                    'quantity': item.get('quantity', 1),
                    'price': product.price
                })
            
            created_orders = []
            for store_id, items in store_items.items():
                store = get_object_or_404(Store, id=store_id)
                subtotal = sum(item['price'] * item['quantity'] for item in items)
                
                order = Order.objects.create(
                    buyer=request.user,
                    store=store,
                    status='pending',
                    subtotal=subtotal,
                    delivery_fee=0,  # Vellon hub transfers are free for now
                    platform_fee=0,
                    total_amount=subtotal,
                    delivery_address=request.POST.get('hub', 'Vellon Central Hub'),
                    delivery_location="On-Pickup Point",
                    delivery_method="Hub Pickup",
                    buyer_phone=request.user.phone_number or "0000000000"
                )
                
                for item in items:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        quantity=item['quantity'],
                        price_at_purchase=item['price']
                    )
                created_orders.append(order)
            
            messages.success(request, f"Successfully placed {len(created_orders)} orders! Sellers have been notified.")
            return render(request, 'orders/success.html', {'orders': created_orders})
            
        except Exception as e:
            messages.error(request, f"Error processing checkout: {str(e)}")
            return redirect('product_list')

    return render(request, 'orders/checkout.html')

@login_required
def order_history_view(request):
    orders = Order.objects.select_related('store').filter(buyer=request.user).order_by('-created_at')
    return render(request, 'orders/history.html', {'orders': orders})

@login_required
def order_detail_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order.buyer != request.user and not request.user.is_staff:
        # Check if user is the store owner
        if not (request.user.is_seller and order.store.owner == request.user):
            messages.error(request, "You do not have permission to view this order.")
            return redirect('home')
            
    return render(request, 'orders/detail.html', {'order': order})

@login_required
def update_order_status(request, pk, status):
    order = get_object_or_404(Order, pk=pk)
    
    # Check if user owns the store
    if order.store.owner != request.user:
        messages.error(request, "Unauthorized.")
        return redirect('home')
    
    valid_statuses = ['accepted', 'preparing', 'in_transit', 'delivered', 'rejected', 'cancelled']
    if status in valid_statuses:
        order.status = status
        if status == 'accepted':
            order.seller_accepted_at = timezone.now()
        elif status == 'rejected':
            order.seller_rejected_at = timezone.now()
        order.save()
        messages.success(request, f"Order status updated to {status.replace('_', ' ')}.")
    else:
        messages.error(request, "Invalid status.")
        
    return redirect('order_detail', pk=pk)
