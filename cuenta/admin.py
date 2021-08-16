from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Perfil
# Register your models here.

class PerfilAdmin(UserAdmin):
    # search_fields = ['username', 'first_name', 'last_name']
    list_display = [
    'username', 'first_name',
     'last_name', 'birthday',
     'is_staff', 'is_superuser']

    fieldsets = (
        ('Usuario',
            {'fields': ('username', 'password')}),
        ('Información Personal',
            {'fields': (
                'first_name',
                'last_name',
                'email',

            )}),
        ("otros datos",
            {'fields':(
                'birthday',
            )}),
        ('Permisos',
            {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',

        )}),
    )

admin.site.register(Perfil, PerfilAdmin)