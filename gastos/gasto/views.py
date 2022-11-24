from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from gasto.models import Gasto
from gasto.GastoForm import GastosForm

# Create your views here.

class GastoCreatedView(CreateView):
    model = Gasto
    form_class = GastosForm
    template_name = 'gasto/gastos_add.html'
    success_url = reverse_lazy('create')