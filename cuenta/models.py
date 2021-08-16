from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class Perfil(models.Model):
#     birthday = models.DateField()
#     usuario = models.OneToOneField(User)

class Perfil(AbstractUser):
    birthday = models.DateField(null=True)