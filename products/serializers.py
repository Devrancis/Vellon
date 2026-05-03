from rest_framework import serializers
from .models import Category, Product, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'icon', 'parent']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_primary']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    store_name = serializers.ReadOnlyField(source='store.name')
    category_name = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = Product
        fields = [
            'id', 'store', 'store_name', 'category', 'category_name',
            'name', 'slug', 'description', 'price', 'condition',
            'quantity_available', 'is_active', 'images', 'rating_average',
            'created_at'
        ]
        read_only_fields = ['id', 'store', 'rating_average', 'created_at']

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'category', 'name', 'slug', 'description', 'price', 
            'condition', 'quantity_available', 'track_inventory'
        ]
