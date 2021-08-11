from django.db.models import fields
from empresa.models import Departamento
from django import forms
from django.db import models
from .models import Departamento, Empleado

class BusquedaForm(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    otro = forms.EmailField()

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ("nombre",)

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
