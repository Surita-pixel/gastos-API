from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.db.models import Sum

from django.http import JsonResponse, HttpResponse

from django.contrib.auth.models import User

from gasto.models import Gasto
from gasto.GastoForm import GastosForm


#from users.models import Perfil

# Create your views here.

def home(request):
    datos = {'messege': 'pong!'}
    return JsonResponse(datos)

def lista_gastos(request):
    gastos = list(Gasto.objects.values())
    if len(gastos) > 0:
        datos = {
            'messege': 'success',
            'gastos': gastos
            }
    
    else: 
        datos = {
            'messege': "gastos don't found"
        }
    
    return JsonResponse(datos)

def prueba(request):
    if request.user.is_authenticated:
        datos = {
            'messege': 'success',
            'gastos': 'pongo'
            }
    
    else: 
        datos = {
            'messege': "inicia sesion"
        }
    return JsonResponse(datos)

def total(request):
    gastos_totales = Gasto.objects.aggregate(Sum('importe'))
    dato = {
        'total': gastos_totales
    }
    return JsonResponse(dato)

def entrada_gasto(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            gasto = GastosForm(request.POST)
            if gasto.is_valid():
                gasto = gasto.save(commit=False)
                gasto.usuario = User.objects.get(id=request.user.id) 
                gasto.save()
                return redirect('list')

                
        else: 
            gasto = GastosForm()
    else:
        return render(request, 'gasto/no_authenticated_user.html')
    
    return render(request, 'gasto/agregar_gasto.html', {'form':gasto})
