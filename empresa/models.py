from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return "Departamento: " + self.nombre

class Empleado(models.Model):
    dni = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    sueldo = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    fecha_nacimiento = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, related_name="empleados")

