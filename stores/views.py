from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orders.models import Order
from rest_framework import generics, permissions
from .models import Store
from .serializers import StoreSerializer, StoreCreateSerializer
from .forms import StoreForm, StoreCreateForm

class StoreListView(generics.ListAPIView):
    queryset = Store.objects.filter(is_active=True, verification_status='approved')
    serializer_class = StoreSerializer
    # ... extensions ...

def store_list_view(request):
    stores = Store.objects.filter(is_active=True, verification_status='approved')
    return render(request, 'stores/store_list.html', {'stores': stores})

def store_detail_view(request, slug):
    store = get_object_or_404(Store, slug=slug, is_active=True)
    return render(request, 'stores/store_detail.html', {'store': store})

class MyStoreView(generics.RetrieveUpdateAPIView):
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return Store.objects.get(owner=self.request.user)

class StoreCreateView(generics.CreateAPIView):
    serializer_class = StoreCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@login_required
def seller_dashboard_view(request):
    try:
        store = Store.objects.get(owner=request.user)
    except Store.DoesNotExist:
        messages.info(request, "You need to create a store first.")
        return redirect('store_list')
    
    orders = Order.objects.select_related('buyer').filter(store=store).order_by('-created_at')
    context = {
        'store': store,
        'orders': orders,
        'pending_orders': orders.filter(status='pending').count(),
        'total_sales': sum(o.total_amount for o in orders.filter(status='completed'))
    }
    return render(request, 'stores/dashboard.html', context)

@login_required
def store_settings_view(request):
    store = get_object_or_404(Store, owner=request.user)
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            form.save()
            messages.success(request, "Store settings updated successfully!")
            return redirect('seller_dashboard')
    else:
        form = StoreForm(instance=store)
    
    return render(request, 'stores/store_form.html', {'form': form, 'store': store})

@login_required
def store_create_html_view(request):
    try:
        # If the user already has a store, redirect to dashboard
        store = Store.objects.get(owner=request.user)
        return redirect('seller_dashboard')
    except Store.DoesNotExist:
        pass

    if request.method == 'POST':
        form = StoreCreateForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            if not store.slug:
                from django.utils.text import slugify
                store.slug = slugify(store.name)
            store.save()
            
            # Set user as seller
            request.user.is_seller = True
            request.user.save()
            
            messages.success(request, "Your store has been created successfully! Welcome to the merchant fleet.")
            return redirect('seller_dashboard')
    else:
        form = StoreCreateForm()
        
    return render(request, 'stores/store_form.html', {'form': form, 'title': 'Create Your Store'})

