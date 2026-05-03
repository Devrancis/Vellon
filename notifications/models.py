from django.db import models
from django.conf import settings

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('order_update', 'Order Update'),
        ('new_message', 'New Message'),
        ('price_drop', 'Price Drop'),
        ('system', 'System Alert'),
    )
    
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_notifications', on_delete=models.SET_NULL, null=True, blank=True)
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['recipient', 'is_read']),
        ]

    def __str__(self):
        return f"{self.notification_type} for {self.recipient.username}"
