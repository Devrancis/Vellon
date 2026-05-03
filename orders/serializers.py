from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price_at_purchase']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    store_name = serializers.ReadOnlyField(source='store.name')
    
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'buyer', 'store', 'store_name',
            'status', 'total_amount', 'delivery_address', 
            'items', 'created_at'
        ]
        read_only_fields = ['id', 'order_number', 'buyer', 'total_amount', 'created_at']
