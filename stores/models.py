from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class Store(models.Model):
    VERIFICATION_STATUS = [
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('suspended', 'Suspended'),
    ]
    
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True) # URL identifier
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = CloudinaryField('image', blank=True)
    banner = CloudinaryField('image', blank=True)
    
    # Verification
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_STATUS, default='pending')
    verification_notes = models.TextField(blank=True)
    verified_at = models.DateTimeField(null=True)
    verified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='verified_stores', on_delete=models.SET_NULL)
    matric_card = CloudinaryField('image') # For verification
    id_document = CloudinaryField('image', blank=True)
    
    # Contact
    whatsapp = models.CharField(max_length=15)
    phone = models.CharField(max_length=15, blank=True)
    
    # Settings
    is_active = models.BooleanField(default=True)
    allow_delivery = models.BooleanField(default=True)
    delivery_locations = models.JSONField(default=list) # List of hostels/areas
    
    # Stats (denormalized for performance)
    total_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_orders = models.IntegerField(default=0)
    acceptance_rate = models.FloatField(default=0)
    rating_average = models.FloatField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def update_rating(self):
        # Implementation to update rating from Review model
        pass

    class Meta:
        indexes = [
            models.Index(fields=['verification_status', 'is_active']),
            models.Index(fields=['slug']),
        ]
