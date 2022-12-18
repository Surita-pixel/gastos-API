from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.db.models import Sum

from django.http import JsonResponse, HttpResponse

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
    if Perfil.is_active() == True:
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
    if request.method == "POST":
        form = GastosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else: 
        form = GastosForm()
    
    return render(request, 'gasto/agregar_gasto.html', {'form':form})
