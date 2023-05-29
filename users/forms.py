from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-register'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-register'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-register'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-register'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
