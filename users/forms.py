from django import forms  
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email", 'password1', 'password2', 'role', 'name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email", 'role', 'name')


class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = CustomUser  
        fields = ('email', 'name', 'password1', 'password2') 