from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Usuario, Perfil

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Usuario
        exclude = (
            'is_staff',
            'is_superuser',
            'last_login'
        )