from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price_at_purchase')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'buyer', 'store', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'payment_status')
    search_fields = ('order_number', 'buyer__username', 'store__name')
    inlines = [OrderItemInline]
    readonly_fields = ('order_number', 'created_at', 'updated_at')
