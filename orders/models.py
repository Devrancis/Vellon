from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
import uuid

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Seller Acceptance'),
        ('accepted', 'Accepted by Seller'),
        ('preparing', 'Preparing Order'),
        ('in_transit', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('completed', 'Completed'),
        ('disputed', 'Disputed'),
        ('rejected', 'Rejected by Seller'),
        ('cancelled', 'Cancelled'),
    ]
    
    # Parties
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases', on_delete=models.CASCADE)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)
    
    # Order Details
    order_number = models.CharField(max_length=20, unique=True) # Auto-generated
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Pricing
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Delivery Info
    delivery_address = models.TextField()
    delivery_location = models.CharField(max_length=200) # Hostel/area name
    delivery_method = models.CharField(max_length=100)
    delivery_notes = models.TextField(blank=True)
    estimated_delivery = models.DateTimeField(null=True)
    
    # Buyer Contact
    buyer_phone = models.CharField(max_length=15)
    buyer_whatsapp = models.CharField(max_length=15, blank=True)
    
    # Seller Response (24-hour window)
    seller_response_deadline = models.DateTimeField()
    seller_accepted_at = models.DateTimeField(null=True)
    seller_rejected_at = models.DateTimeField(null=True)
    rejection_reason = models.TextField(blank=True)
    auto_rejected = models.BooleanField(default=False)
    
    # Delivery Confirmation (Escrow-like)
    seller_marked_delivered_at = models.DateTimeField(null=True)
    buyer_confirmed_delivery_at = models.DateTimeField(null=True)
    auto_completed = models.BooleanField(default=False) # Auto-complete after 72hrs
    
    # Dispute Management
    dispute_reason = models.TextField(blank=True)
    dispute_resolved = models.BooleanField(default=False)
    resolution_notes = models.TextField(blank=True)
    
    # Payment
    payment_method = models.CharField(max_length=50, default='pay_on_delivery')
    payment_status = models.CharField(max_length=20, default='unpaid')
    payment_reference = models.CharField(max_length=100, blank=True)
    paid_at = models.DateTimeField(null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def generate_order_number(self):
        return str(uuid.uuid4().hex[:10].upper())

    def save(self, *args, **kwargs):
        # Generate order number
        if not self.order_number:
            self.order_number = self.generate_order_number()
        # Set seller response deadline (24 hours)
        if not self.seller_response_deadline:
            self.seller_response_deadline = timezone.now() + timedelta(hours=24)
        super().save(*args, **kwargs)
        
    class Meta:
        indexes = [
            models.Index(fields=['buyer', '-created_at']),
            models.Index(fields=['store', 'status']),
            models.Index(fields=['status', 'seller_response_deadline']),
        ]

    # Logic Methods
    def accept_order(self, seller_user):
        # Check permissions and state
        pass

    def auto_reject_if_expired(self):
        # Logic for auto-rejection
        pass


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        # Reserve stock when order is created
        if not self.pk:
            if not self.product.reduce_stock(self.quantity):
                raise ValueError(f"Insufficient stock for {self.product.name}")
        super().save(*args, **kwargs)
