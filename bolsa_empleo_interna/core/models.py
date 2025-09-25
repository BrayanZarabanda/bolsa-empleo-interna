from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    ROLES = (('empresa', 'Empresa'),
             ('aspirante','Aspirante'),
             )
    telefono = models.CharField(max_length=20, blank=True, null=True)
    documento = models.CharField(max_length=50, unique=True, blank=True, null=True)
    rol = models.CharField(max_length=10, choices=ROLES)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=False, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['documento', 'first_name', 'last_name']

    def __str__(self):
        return self.email

class Vacante(models.Model):
    nombre_vacante = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_vacante
