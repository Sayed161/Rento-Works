from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomerSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class CompanyAdminSignUpForm(UserCreationForm):
    company_name = forms.CharField(
        max_length=255, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Company Name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter your email'})
    )

    class Meta:
        model = User
        fields = ('company_name','email', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'required': 'required'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'required': 'required'
        })
    )