from django.contrib import admin
from .models import Category, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'order')
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'store', 'price', 'quantity_available', 'is_active')
    list_filter = ('is_active', 'condition', 'category')
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('name',)}
