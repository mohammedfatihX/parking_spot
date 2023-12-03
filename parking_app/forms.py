# parking_app/forms.py
from django import forms

class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)
