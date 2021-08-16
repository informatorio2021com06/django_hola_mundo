from django.urls import path
from . import views

urlpatterns = [
    #path("", views.inicio),
    path("departamentos/", views.departamentos, name='lista_dptos'),
    path("departamento/<int:id>/detalle", views.departamento,name="detalle_departamento"),
    # crear departamento
    path("departamentos/nuevo/", views.nuevo_dpto, name='nuevo_dpto'),
    # editar departament
     path("departamento/<int:id>/editar", views.editar_dpto,name="editar_dpto"),
    # borrar departamento
    path("empleados/", views.empleados,name="lista_empleados"),
    path("empleados/nuevo/", views.nuevo_empleado, name='nuevo_empleado'),
    path("empleados/<int:id>/detalle", views.empleado,name="detalle_empleado"),


]
