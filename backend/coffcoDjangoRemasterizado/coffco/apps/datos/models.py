from django.db import models
from django.db.models import SET_NULL
from apps.versiones.models import Versiones

class Datos(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.FloatField()
    estado = models.BooleanField()
    fk_id_formato = models.ForeignKey(Versiones, on_delete = SET_NULL, null=True)
    
    
    def __str__(self):
        return self.nombre

