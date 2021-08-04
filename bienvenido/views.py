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

def saludar(request):
    variable = 5+7
    return HttpResponse("hola mundo" + str(variable))