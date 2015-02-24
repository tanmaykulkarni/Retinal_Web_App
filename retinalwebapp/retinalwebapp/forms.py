'''
Django Models and model form tutorial
https://www.youtube.com/watch?v=f0uZqPNijCw
'''

from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
          'password': forms.PasswordInput(),
        } 


class LoginForm(forms.Form):
   username = forms.CharField(max_length=100, initial='username')
   password = forms.CharField(widget=forms.PasswordInput, initial='password')
