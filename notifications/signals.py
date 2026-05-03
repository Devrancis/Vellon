from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order
from messaging.models import Message
from .models import Notification

@receiver(post_save, sender=Order)
def order_status_notification(sender, instance, created, **kwargs):
    if not created:  # Status update
        Notification.objects.create(
            recipient=instance.buyer,
            notification_type='order_update',
            title=f"Order Update: #{instance.order_number}",
            description=f"Your order from {instance.store.name} is now {instance.status.replace('_', ' ')}.",
            link=f"/orders/{instance.id}/"
        )

@receiver(post_save, sender=Message)
def new_message_notification(sender, instance, created, **kwargs):
    if created:
        recipient = instance.conversation.seller if instance.sender == instance.conversation.buyer else instance.conversation.buyer
        Notification.objects.create(
            recipient=recipient,
            sender=instance.sender,
            notification_type='new_message',
            title=f"New message from {instance.sender.username}",
            description=instance.content[:50] + "..." if len(instance.content) > 50 else instance.content,
            link=f"/messages/{instance.conversation.id}/"
        )
