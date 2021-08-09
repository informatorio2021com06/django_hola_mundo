from django.urls import path
from . import views

urlpatterns = [
    #path("", views.inicio),
    path("bienvenido/", views.inicio, name="inicio"),
    path("saludar/<str:nombre>/", views.saludar),
    path("numero/<int:numero_x>/", views.ver_numero),
    path("sumar/<int:a>/<int:b>/", views.sumar),
]
