from django.shortcuts import render, redirect
from django.views.generic import CreateView

from django.db.models import Sum

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound

from django.contrib.auth.models import User

from gasto.models import Gasto
from gasto.GastoForm import GastosForm

# Create your views here.

def home(request):
    """
    A view that renders the home page for the user. If the user is authenticated, render the 'gasto/home.html' template.
    If the user is not authenticated, render the 'gasto/no_authenticated_user.html' template.
    """
    if request.user.is_authenticated:
        return render(request, 'gasto/home.html')
    
    else:
        return render(request, 'gasto/no_authenticated_user.html')

def lista_gastos(request):
    """
    A view that renders a list of expenses for the authenticated user. If the user is not authenticated, 
    render the 'gasto/no_authenticated_user.html' template.
    """
    if request.user.is_authenticated:
        user_id =  User.objects.get(id=request.user.id)
        gastos = Gasto.objects.filter(usuario_id=user_id)

        if len(gastos) > 0:
            return render(
                request, 
                'gasto/gastos_list.html', 
                {'gastos': gastos}
                )

        else:
            dato = {'messege':'no se ha encontrado gasto registrado'}
            return HttpResponse(dato)
    else:
        return render(request, 'gasto/no_authenticated_user.html')

def total(request):
    """
    A view that returns the total sum of expenses as a JSON object.
    """
    gastos_totales = Gasto.objects.aggregate(Sum('importe'))
    dato = {
        'total': gastos_totales
    }
    return JsonResponse(dato)

def entrada_gasto(request):
    """
    A view that handles the rendering and submission of a form for entering a new expense. If the user is not authenticated, 
    render the 'gasto/no_authenticated_user.html' template.
    """
    if request.user.is_authenticated:
        if request.method == "POST":
            # If the request method is POST, process the form submission.
            gasto = GastosForm(request.POST)
            if gasto.is_valid():
                gasto = gasto.save(commit=False)
                gasto.usuario = User.objects.get(id=request.user.id) 
                gasto.save()
                return redirect('list')
                
        else: 
            # If the request method is not POST, render an empty form.
            gasto = GastosForm()
    else:
        return render(request, 'gasto/no_authenticated_user.html')
    
    return render(request, 'gasto/agregar_gasto.html', {'form':gasto})
