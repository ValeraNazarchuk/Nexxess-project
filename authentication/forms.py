from django.forms import ModelForm, TextInput, PasswordInput, NumberInput, FileInput
from django import forms


class CustomLoginForm(forms.Form):
    login = forms.CharField(widget=TextInput(attrs={"class": "authentication__box-input"}))
    password = forms.CharField(widget=PasswordInput(attrs={"class": "authentication__box-input"}))