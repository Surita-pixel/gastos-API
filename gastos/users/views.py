# Django
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

#formulario y modelos
from django.contrib.auth.models import User
from .forms import SignUpForm

# Create your views here.

class SignUpView(CreateView):
    """
    A class-based view that handles the rendering and submission of a form for user registration.
    """
    form_class = SignUpForm
    template_name = 'users/register.html'
    success_url = '/'

class SignInView(LoginView):
    """
    A class-based view that handles the rendering and submission of a form for user login.
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # If the user is already authenticated, render the 'users/logued.html' template.
            return render(request, 'users/logued.html')
        
        else:
            # If the user is not authenticated, render the 'users/login.html' template.
            self.template_name = 'users/login.html'
            return super().get(request, *args, **kwargs)

class LogOut(LogoutView):
    """
    A class-based view that handles the logout process for a user.
    """
    def logout(self):
        # Upon successful logout, redirect the user to '/'.
        return redirect('/')
