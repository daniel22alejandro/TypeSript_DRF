from django.db import models
from django.db.models import SET_NULL
from apps.versiones.models import Versiones
from apps.datos.models import Datos
from apps.servicios.models import Servicios


class Detalle(models.Model):
    fk_id_formato = models.ForeignKey(Versiones, on_delete = SET_NULL, null=True)
    fk_id_datos = models.ForeignKey(Datos, on_delete = SET_NULL, null=True)
    valor = models.FloatField()
    fk_id_servicios = models.ForeignKey(Servicios, on_delete = SET_NULL, null=True)

    def __str__(self):
        return f"Detalle {self.id_detalle}"
