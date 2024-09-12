# my_django_app/forms.py
from django import forms

class LoginForm(forms.Form):
    id = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su R. académico'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}))

class RegistroForm(forms.Form):
    id = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su R. académico'}))
    nombres = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}))
    apellidos = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}))
