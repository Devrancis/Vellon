from django.urls import path
from .views import ProductListView, CategoryListView, ProductCreateView, product_list_view, product_detail_view

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('api/', ProductListView.as_view(), name='product-list-api'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<slug:slug>/', product_detail_view, name='product_detail'),
]
