from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    name = forms.CharField(label='name')

class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput)