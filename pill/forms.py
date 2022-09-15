from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from pill.models import User



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', "role"]


class LoginForm(forms.Form):
    username = forms.EmailField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)