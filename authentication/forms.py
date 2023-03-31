from django.forms import ModelForm, TextInput, PasswordInput, NumberInput, FileInput
from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#


class CustomLoginForm(forms.Form):
    login = forms.CharField(widget=TextInput(attrs={"class": "authentication__box-input"}))
    password = forms.CharField(widget=PasswordInput(attrs={"class": "authentication__box-input"}))



# class CustomLoginForm_2(forms.Form):
#     login = forms.CharField(widget=TextInput(attrs={"class": "authentication__box-input"}),required=True)
#     password = forms.CharField(widget=PasswordInput(attrs={"class": "authentication__box-input"}),required=True)


# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')
#     class Meta:
#         model = User
#         fields =('username', 'email', 'password1', 'password2')
