
#Create User Login Form

from django import forms

class loginForm(forms.Form):
        #email = forms.CharField(level='',required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

        email = forms.EmailField(label='',
                                 widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Enter Email'}))

        password = forms.CharField(max_length=32,label='', widget=forms.PasswordInput(attrs={"class": 'form-control', 'placeholder': 'Enter Password'}))