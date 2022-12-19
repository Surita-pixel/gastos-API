# Django
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

#formulario y modelos
from django.contrib.auth.models import User
from .forms import SignUpForm

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'users/register.html'
    success_url = '/'

class SignInView(LoginView):
    template_name = 'users/login.html'

class LogOut(LogoutView):
    def logout(self):
        return redirect('/')