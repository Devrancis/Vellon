from django.db import models
from django.conf import settings

class Review(models.Model):
    order = models.OneToOneField('orders.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) # 1-5 stars
    comment = models.TextField(blank=True)
    
    # Seller can respond
    seller_response = models.TextField(blank=True)
    seller_responded_at = models.DateTimeField(null=True)
    
    is_verified_purchase = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update product and store ratings
        self.product.update_rating()
        self.store.update_rating()
