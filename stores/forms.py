from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description', 'phone', 'whatsapp', 'logo', 'banner']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3 fw-bold'}),
            'description': forms.Textarea(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3', 'rows': 4}),
            'phone': forms.TextInput(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3'}),
        }

class StoreCreateForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'slug', 'description', 'phone', 'whatsapp', 'logo', 'banner', 'matric_card']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3 fw-bold', 'placeholder': 'Enter your brand name'}),
            'slug': forms.TextInput(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3', 'placeholder': 'e.g. my-brand-name'}),
            'description': forms.Textarea(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3', 'rows': 4, 'placeholder': 'Tell us about your store...'}),
            'phone': forms.TextInput(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3', 'placeholder': '+234...'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3', 'placeholder': '+234...'}),
        }

