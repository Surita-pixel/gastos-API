from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from .form import SignupForm
from .models import Usuario, Perfil

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm()
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    return render(request, 'users/registrate.html', {'form':form})