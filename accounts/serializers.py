from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'matric_number', 
            'phone_number', 'whatsapp_number', 'is_seller', 
            'profile_image', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'phone_number', 
            'whatsapp_number', 'profile_image'
        ]
