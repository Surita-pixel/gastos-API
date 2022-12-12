from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Usuario, Perfil

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Usuario
        fiels = (
            '__all__'
        )