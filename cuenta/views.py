from django import forms
from django.shortcuts import redirect, render, resolve_url
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditarPerfilForm, NuevoPerfilForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def crear_usuario(request):
    if request.user.is_authenticated:
        return redirect("inicio")
    form = NuevoPerfilForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            #return redirect("iniciar_sesion")
            login(request, user)
            
            return redirect("inicio")
    contexto = {"form":form}
    return render(request, "cuenta/nuevo_usuario.html",contexto)

def editar_usuario(request):
    if not request.user.is_authenticated:
        return redirect("iniciar_sesion")

    perfil = request.user
    form = EditarPerfilForm(instance=perfil)
    if request.method == "POST":
        form = EditarPerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            user = form.save()
            return redirect("inicio")
    contexto = {"form":form}
    return render(request, "cuenta/nuevo_usuario.html",contexto)

def iniciar_sesion(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            login(request,user)

            return redirect("inicio")
            
        print("errores: ", form.errors)
    contexto = {"form":form}
    return render(request, "cuenta/login.html",contexto)

def cerrar_sesion(request):
    if request.user.is_authenticated():
        logout(request, request.user)
    return redirect("inicio")

def pass_cambiada(request):
    return redirect("inicio")