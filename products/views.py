from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Product, Category
from .serializers import ProductSerializer, ProductCreateSerializer, CategorySerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm
from django.utils.text import slugify

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    # ... existing filters ...

def product_list_view(request):
    products = Product.objects.select_related('category', 'store').filter(is_active=True)
    categories = Category.objects.all()
    
    # Advanced Filtering
    q = request.GET.get('q')
    if q:
        products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))
        
    cat_id = request.GET.get('category')
    if cat_id:
        products = products.filter(category_id=cat_id)
        
    min_price = request.GET.get('min_price')
    if min_price:
        products = products.filter(price__gte=min_price)
        
    max_price = request.GET.get('max_price')
    if max_price:
        products = products.filter(price__lte=max_price)
        
    sort = request.GET.get('sort')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    else:
        products = products.order_by('-created_at')

    context = {
        'products': products, 
        'categories': categories,
        'current_q': q,
        'current_cat': int(cat_id) if cat_id else None,
        'current_sort': sort
    }
    return render(request, 'products/product_list.html', context)

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'products/product_detail.html', {'product': product})

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_class = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        from stores.models import Store
        store = Store.objects.get(owner=self.request.user)
        serializer.save(store=store)

@login_required
def product_create_view(request):
    try:
        from stores.models import Store
        store = Store.objects.get(owner=request.user)
    except Store.DoesNotExist:
        messages.error(request, "You must create a store first.")
        return redirect('store_list')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store
            product.slug = slugify(product.name)
            product.save()
            messages.success(request, f"Product '{product.name}' listed successfully!")
            return redirect('seller_dashboard')
    else:
        form = ProductForm()
    
    return render(request, 'products/product_form.html', {'form': form, 'title': 'List New Product'})

@login_required
def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.store.owner != request.user:
        messages.error(request, "You don't have permission to edit this product.")
        return redirect('seller_dashboard')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('seller_dashboard')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/product_form.html', {'form': form, 'title': f'Edit {product.name}'})
