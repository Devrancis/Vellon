from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'quantity_available', 'track_inventory', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3 fw-bold', 'placeholder': 'e.g. MacBook Pro 2021'}),
            'category': forms.Select(attrs={'class': 'form-select border-dark border-2 rounded-0 py-3 fw-bold'}),
            'description': forms.Textarea(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3', 'rows': 4, 'placeholder': 'Detailed item description...'}),
            'price': forms.NumberInput(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3 fw-bold'}),
            'quantity_available': forms.NumberInput(attrs={'class': 'form-control border-dark border-2 rounded-0 py-3 fw-bold'}),
            'track_inventory': forms.CheckboxInput(attrs={'class': 'form-check-input border-dark'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input border-dark'}),
        }
