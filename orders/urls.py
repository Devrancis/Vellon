from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('history/', views.order_history_view, name='order_history'),
    path('<int:pk>/', views.order_detail_view, name='order_detail'),
    path('<int:pk>/status/<str:status>/', views.update_order_status, name='update_order_status'),
]
