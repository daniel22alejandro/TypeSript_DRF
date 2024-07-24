from django.db import models
from django.db.models import SET_NULL
from apps.finca.models import Finca

class Muestra(models.Model):
    cantidad = models.FloatField()
    fk_id_finca = models.ForeignKey(Finca, on_delete = SET_NULL, null=True)
    fecha_muestra = models.DateField(null=True)

    def __str__(self):
        return f"Muestra #{self.id}"

