from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text= 'Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text= 'Optional')
    email = forms.EmailField(max_length=250, help_text= 'Requerido')
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

