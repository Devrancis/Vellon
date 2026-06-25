from django.urls import path
from .views import (
    MyStoreView, StoreCreateView, store_list_view, store_detail_view,
    StoreListView, seller_dashboard_view, store_settings_view, store_create_html_view
)

urlpatterns = [
    path('', store_list_view, name='store_list'),
    path('api/', StoreListView.as_view(), name='store-list-api'),
    path('create/', store_create_html_view, name='store_create'),
    path('api/create/', StoreCreateView.as_view(), name='store_create_api'),
    path('my-store/', MyStoreView.as_view(), name='my_store'),
    path('portal/dashboard/', seller_dashboard_view, name='seller_dashboard'),
    path('portal/settings/', store_settings_view, name='store_settings'),
    path('<slug:slug>/', store_detail_view, name='store_detail'),
]

