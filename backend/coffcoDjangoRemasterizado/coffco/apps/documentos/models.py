from django.db import models
from django.db.models import SET_NULL
from apps.users.models import User

class Documentos(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_carga = models.DateField()
    fk_id_usuarios = models.ForeignKey(User, on_delete = SET_NULL, null=True)
    descripcion = models.CharField(max_length=200)
    formato = models.CharField(max_length=50, null=True, blank=True)
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    estado = models.CharField(max_length=8, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return self.nombre
