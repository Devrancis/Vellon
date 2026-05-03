from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer, UserUpdateSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UserUpdateSerializer
        return UserSerializer
