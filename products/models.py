from django.db import models
from django.db.models import Index
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50) # Emoji or icon class
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CONDITION_CHOICES = [
        ('new', 'Brand New'),
        ('like_new', 'Like New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
    ]
    
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    # Basic Info
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='new')
    
    # Inventory
    track_inventory = models.BooleanField(default=True)
    quantity_available = models.IntegerField(default=0)
    low_stock_threshold = models.IntegerField(default=5)
    allow_backorders = models.BooleanField(default=False)
    
    # Visibility
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    featured_until = models.DateTimeField(null=True, blank=True)
    
    # SEO & Discovery
    tags = models.JSONField(default=list)
    views_count = models.IntegerField(default=0)
    
    # Stats
    sold_count = models.IntegerField(default=0)
    rating_average = models.FloatField(default=0)
    review_count = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['store', 'slug']
        indexes = [
            Index(fields=['store', 'is_active']),
            Index(fields=['category', 'price']),
            Index(fields=['-created_at']),
            Index(fields=['is_featured', '-created_at']),
        ]

    def reduce_stock(self, quantity):
        if not self.track_inventory:
            return True
        if self.quantity_available >= quantity:
            self.quantity_available -= quantity
            self.save()
            return True
        return False

    def restore_stock(self, quantity):
        if self.track_inventory:
            self.quantity_available += quantity
            self.save()

    def update_rating(self):
        # Implementation to update rating from Review model
        pass

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    order = models.IntegerField(default=0)
    is_primary = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['order']
