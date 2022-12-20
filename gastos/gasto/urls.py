from django.urls import path
from .views import entrada_gasto, lista_gastos, total
urlpatterns = [
    path('add/', entrada_gasto, name='add'),
    path('list/', lista_gastos, name='list'),
    path('total/', total, name='total'),
]