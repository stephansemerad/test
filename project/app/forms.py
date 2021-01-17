from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=128)
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput())