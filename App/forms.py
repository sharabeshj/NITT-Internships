from django import forms
from django.contrib.auth.models import User
from App.models import Profile

class LoginForm(forms.ModelForm):
    
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('resume','cover_letter','lor')