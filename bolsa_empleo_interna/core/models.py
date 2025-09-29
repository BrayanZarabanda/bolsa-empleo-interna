from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')
        if 'rol' not in extra_fields:
            extra_fields.setdefault('rol', 'empresa')

        return self._create_user(email, password, **extra_fields)



class Usuario(AbstractUser):

    username = None  # Elimina el campo username predeterminado

    ROLES = (('empresa', 'Empresa'),
             ('aspirante','Aspirante'),
             )
    telefono = models.CharField(max_length=20, blank=True, null=True)
    documento = models.CharField(max_length=50, unique=True, blank=True, null=True)
    rol = models.CharField(max_length=10, choices=ROLES)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['documento', 'first_name', 'last_name']

    objects = UsuarioManager()
    # Para que el admin muestre el email en lugar del username

    def __str__(self):
        return self.email

class Vacante(models.Model):
    nombre_vacante = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_vacante
