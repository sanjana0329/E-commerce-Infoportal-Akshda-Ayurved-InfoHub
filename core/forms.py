from accounts.models import CustomUser
from core.models import *
from django import forms
from django.contrib.admin import widgets
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import *


class ContactUsForm(forms.ModelForm):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Full Name",
                "class": "form-control",
                "aria-label": "Full Name",
                "aria-describedby": "fullname-addon",
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
                "aria-label": "Email",
                "aria-describedby": "email-addon",
            }
        ))
    contact_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Contact Number",
                "class": "form-control",
                "aria-label": "Contact Number",
                "aria-describedby": "contactno-addon",
            }
        ))
    comments = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Message",
                "class": "form-control",
                "aria-label": "Comments",
                "aria-describedby": "comments-addon",
                "rows": 4,
            }
        ))

    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'contact_no', 'comments']