from django.shortcuts import render
from .models import Departamento, Empleado
# Create your views here.
def departamentos(request):
    departamentos = Departamento.objects.all()
    template = "empresa/departamentos.html"
    contexto = {
        "departamentos":departamentos
    }
    return render(request, template, contexto)


def empleados(request):
    empleados = Empleado.objects.all()
    template = "empresa/empleados.html"
    contexto = {
        "empleados":empleados
    }
    return render(request, template, contexto)

def empleado(request, id):
    empleado = Empleado.objects.get(pk=id)
    template = "empresa/empleado.html"
    contexto = {
        "empleado":empleado
    }
    return render(request, template, contexto)


def departamento(request, id):
    dpto = Departamento.objects.get(pk=id)
    template = "empresa/dpto.html"
    contexto = {
        "dpto":dpto
    }
    return render(request, template, contexto)
    