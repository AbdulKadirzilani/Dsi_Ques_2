from django.forms import ModelForm, PasswordInput
from django import forms
from .models import Information

class loginForm(forms.Form):
        email = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        password = forms.CharField(max_length=32, widget=forms.PasswordInput)