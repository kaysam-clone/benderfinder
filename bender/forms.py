from django import forms
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['full_name', 'image'] 