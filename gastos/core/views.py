from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeGastosView(TemplateView):
    template_name = 'core/home.html'

class ListGastosView(TemplateView):

    template_name = 'core/gastos_list.html'

