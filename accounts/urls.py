from django.urls import path
from .views import ProfileView, profile_html_view

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/settings/', profile_html_view, name='profile_settings'),
]

