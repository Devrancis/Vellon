from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class Conversation(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='buyer_conversations', on_delete=models.CASCADE)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='seller_conversations', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey('orders.Order', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['buyer', 'seller', 'product']
        indexes = [
            models.Index(fields=['-updated_at']),
        ]

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['conversation', 'created_at']),
        ]
