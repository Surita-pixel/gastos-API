from django import forms
from .models import Gasto

class GastosForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = {
                'nombre',
                'categoria',
                'importe',
                'fecha',
                'descripcion'
        }
        widgets = {
            'categoria':forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(format='%d%m%Y', attrs={'class':'form-control','type':'date'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'importe': forms.NumberInput(attrs={'class':'form-control'}),
            'categoria':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'nombre':'',
            'fecha':'',
            'descripcion':'',
            'importe':'',
            'categoria':'',
        }