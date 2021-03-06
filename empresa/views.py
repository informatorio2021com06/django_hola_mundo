from django.shortcuts import redirect, render
from .models import Departamento, Empleado
from .forms import BusquedaForm, DepartamentoForm, EmpleadoForm
from django.contrib.auth.decorators import login_required, user_passes_test

def usuario_es_staff(user):
    return user.is_staff or user.is_superuser


# Create your views here.
def departamentos(request):
    formulario = BusquedaForm()
    filtro_nombre = request.GET.get("nombre", "")
    departamentos = Departamento.objects.filter(nombre__icontains=filtro_nombre)
    template = "empresa/departamentos.html"
    contexto = {
        "departamentos":departamentos,
        "formulario_busqueda":formulario,

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

def nuevo_dpto(request):
    if not request.user.is_authenticated:
        return redirect("iniciar_sesion")
    if not request.user.is_staff: 
        return redirect("inicio")

    form = DepartamentoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dpto = form.save()
            print("form.save: ", dpto)
            return redirect("detalle_departamento", dpto.id)
    template = "empresa/nuevo_dpto.html"
    contexto = {
        "form":form,
    }
    return render(request, template, contexto)

@login_required
@user_passes_test(usuario_es_staff)
def editar_dpto(request,id):
    dpto = Departamento.objects.get(pk=id)

    form = DepartamentoForm(request.POST or None, instance=dpto)
    if request.method == "POST":
        if form.is_valid():
            dpto = form.save()
            print("form.save: ", dpto)
            return redirect("detalle_departamento", dpto.id)
    template = "empresa/nuevo_dpto.html"
    contexto = {
        "form":form,
    }
    return render(request, template, contexto)

@login_required
@user_passes_test(usuario_es_staff)
def nuevo_empleado(request):
    form = EmpleadoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            emp = form.save()
            print("form.save: ", emp)
            return redirect("detalle_empleado", emp.id)
    template = "empresa/nuevo_empleado.html"
    contexto = {
        "form":form,
    }
    return render(request, template, contexto)




