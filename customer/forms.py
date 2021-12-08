from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from owner.models import Order


class UserRegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

    widgets={
        "first_name":forms.TextInput(attrs={"class":"form-control"}),
        "last_name":forms.TextInput(attrs={"class":"form-control"}),
        "email":forms.EmailInput(attrs={"class":"form-control"}),
        "username":forms.TextInput(attrs={"class":"form-control"}),
    }


class LoginForm(forms.Form):
    user_name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=["product","address","phone_number"]
        widgets={
            "product":forms.Select(attrs={"class":"form-control","readonly":True}),
            "address":forms.Textarea(attrs={"class":"form-control"}),
            "phone_number":forms.NumberInput(attrs={"class":"form-control"})
        }


