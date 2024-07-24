from django.db import models
from django.db.models import SET_NULL
from apps.muestra.models import Muestra
from apps.versiones.models import Versiones


class Servicios(models.Model):
    tipo_servicios = models.CharField(max_length=100)
    fk_id_muestra = models.ForeignKey(Muestra, on_delete = SET_NULL, null=True)
    fk_formato = models.ForeignKey(Versiones, on_delete = SET_NULL, null=True)

    def __str__(self):
        return self.tipo_servicios
