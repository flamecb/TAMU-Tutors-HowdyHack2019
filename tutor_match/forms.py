from django import forms
from django.contrib.auth.forms import UserCreationForm
from tutor_match.models import Tutor
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    u_email = forms.EmailField(label='Email')
    u_password = forms.CharField(label='Password', widget=forms.PasswordInput())

class UserAuthForm(forms.Form):
    u_email = forms.EmailField(label='Email')
    u_password = forms.CharField(label='Password', widget=forms.PasswordInput())

class UserProfileForm(forms.Form):
    u_fullName = forms.CharField(label='Full Name')
    u_classID = forms.CharField(label='Class')
    u_price = forms.DecimalField(max_digits=5, decimal_places=2)
    u_contact = forms.CharField(label='Contact Info')
    u_rating = forms.DecimalField()

class UserSearchForm(forms.Form):
    t_name = forms.CharField(label='Name', required=False)
    t_classID = forms.CharField(label='Class', required=False)
    t_price = forms.DecimalField(min_value=0.0, required = False)
    t_rating = forms.DecimalField(min_value=0.0, required = False)