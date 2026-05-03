from django import forms

class CustomSignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    matric_number = forms.CharField(max_length=20, label='Matric Number', widget=forms.TextInput(attrs={'placeholder': 'Matric Number'}))
    phone_number = forms.CharField(max_length=15, label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.matric_number = self.cleaned_data['matric_number']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
