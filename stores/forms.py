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
