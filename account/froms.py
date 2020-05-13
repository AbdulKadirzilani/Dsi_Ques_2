from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForms(UserCreationForm):

    email = forms.EmailField(label='',widget=forms.TextInput(attrs={"class":'form-control','placeholder':'Enter Emails'}))
    # first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    # last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Last Name'}))

# Convention format for Python django
    class Meta:
        model = User
        fields = ('username','email','password1','password2',)


# By default some condition and instruction for 'username' and 'password1','password2'

    def __init__(self, *args, **kwargs):
        super(RegisterForms, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
        self.fields['username'].label=''
        self.fields['username'].help_text=''

        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
        self.fields['password1'].label=''
        self.fields['password1'].help_text=''

        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirm Password'})
        self.fields['password2'].label=''
        self.fields['password2'].help_text=''

