from django.urls import path
from . import views

urlpatterns = [
    #path("", views.inicio),
    path("departamentos/", views.departamentos, name='lista_dptos'),
    path("departamento/<int:id>/detalle", views.departamento,name="detalle_departamento"),
    path("empleados/", views.empleados,name="lista_empleados"),
    path("empleados/<int:id>/detalle", views.empleado,name="detalle_empleado"),


]
