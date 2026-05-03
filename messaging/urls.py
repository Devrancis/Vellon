from django.urls import path
from . import views

urlpatterns = [
    path('', views.conversation_list_view, name='inbox'),
    path('<int:pk>/', views.chat_detail_view, name='chat_detail'),
    path('start/<int:product_id>/', views.start_conversation_view, name='start_conversation'),
]
