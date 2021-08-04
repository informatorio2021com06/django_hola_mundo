from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("pagina de inicio")

def saludar(request):
    variable = 5+7
    return HttpResponse("hola mundo" + str(variable))