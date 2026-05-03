from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Store
        fields = [
            'id', 'owner', 'name', 'slug', 'description', 
            'logo', 'banner', 'verification_status', 
            'whatsapp', 'phone', 'is_active', 'rating_average',
            'created_at'
        ]
        read_only_fields = ['id', 'owner', 'verification_status', 'rating_average', 'created_at']

class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'slug', 'description', 'whatsapp', 'phone', 'matric_card']
