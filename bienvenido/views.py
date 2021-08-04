from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    contexto = {
        "nombre":"axel",
        "apellido":"pedro",
        "numero":24,
    }
    return render(request, "bienvenido/inicio.html", contexto)
    #return HttpResponse("<h1>Pagina inicio</h1>")

def saludar(request, nombre):
    contexto = {
        "nombre":nombre
    }
    return render(request, "bienvenido/saludar.html", contexto)

def ver_numero(request, numero_x):
    contexto = {
        "numero":numero_x
    }
    return render(request, "bienvenido/inicio.html", contexto)


def sumar(request, a, b):
    resultado = a+b
    contexto = {
        "a":a,
        "b":b,
        "resultado":resultado
    }
    return render(request, "bienvenido/suma.html",contexto)