from django.urls import path
from . import views

urlpatterns = [
    path('', views.notification_list_view, name='notification_list'),
    path('api/unread/', views.api_get_notifications, name='api_unread_notifications'),
    path('mark-read/<int:pk>/', views.mark_read, name='mark_notification_read'),
]
