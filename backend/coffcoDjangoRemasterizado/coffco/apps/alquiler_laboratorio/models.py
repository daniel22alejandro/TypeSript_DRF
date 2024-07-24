from django.db import models
from django.db.models import SET_NULL
from apps.users.models import User

class AlquilerLaboratorio(models.Model):
    fecha_alquiler = models.DateTimeField()
    fk_usuarios = models.ForeignKey(User, on_delete = SET_NULL, null=True)  # Se debe reemplazar por ForeignKey a la tabla de usuarios
    ESTADO_CHOICES = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    )
    estado = models.CharField(max_length=8, choices=ESTADO_CHOICES)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.fecha_alquiler
