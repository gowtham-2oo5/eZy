from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm
from django.contrib.auth.models import User
from django import forms
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        
class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
        
class PasswordResetForm(PasswordResetForm):
    class Meta:
        model = User
        fields = []