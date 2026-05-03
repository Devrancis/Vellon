from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

class User(AbstractUser):
    matric_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    email_verified = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    whatsapp_number = models.CharField(max_length=15, blank=True)
    profile_image = CloudinaryField('image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Must use @futa.edu.ng email
        if self.email and not self.email.endswith('@futa.edu.ng'):
            raise ValidationError('Must use Vellon email')
