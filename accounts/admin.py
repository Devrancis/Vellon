from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'matric_number', 'is_seller', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('matric_number', 'phone_number', 'whatsapp_number', 'is_seller', 'profile_image')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('matric_number', 'phone_number', 'is_seller')}),
    )
