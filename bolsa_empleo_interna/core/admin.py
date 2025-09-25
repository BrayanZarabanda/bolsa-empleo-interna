from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Vacante

# Register your models here.

# Clase para mejorar la visualización del modelo Usuario en el admin
class UsuarioAdmin(UserAdmin):
    # Campos a mostrar en la lista de usuarios
    list_display = ('email', 'first_name', 'last_name', 'rol', 'is_staff')

    # Le decimos al admin que ordene por 'email' porque 'username' ya no existe.
    ordering = ('email',)

    # Campos que se usarán para la creación y edición de usuarios
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields': ('documento', 'telefono', 'rol')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Personalizados', {'fields': ('documento', 'telefono', 'rol')}),
    )

# Registrar los modelos
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Vacante)