from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,Category
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "Name",
            "Email",
            "Telephone",
            "content",
            "city",
            "location",
        ]
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=[
            "category_title",
            "category_logo",
            "Name",
            "Price",
            ]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password',)