from django.contrib.auth.forms import UserCreationForm
from accounts.models import MyUser
from django import forms


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='',
                             widget=forms.EmailInput(
                             attrs={'class': 'form-control', 'placeholder': 'Email'}))

    password1 = forms.CharField(label='',
                                widget=forms.PasswordInput(
                                attrs={'class': 'form-control', 'placeholder': 'Password'}))

    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(
                                attrs={'class': 'form-control', 'placeholder': 'Password confirmation'}))

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['username', 'email', 'avatar', 'password1', 'password2', 'first_name', 'phone_number', 'gender', 'about_me']

        labels = {
            'username': '',
            'first_name': '',
            'phone_number': '',
            'gender': '',
            'about_me': '',
            'avatar': '',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'about_me': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'About me'
            }),
        }
