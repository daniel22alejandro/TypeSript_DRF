from django.db import models
from django.db.models import SET_NULL
from apps.users.models import User
from apps.municipio.models import Municipio




class Finca(models.Model):
    nombre_finca = models.CharField(max_length=50)
    fk_id_municipio = models.ForeignKey(Municipio, on_delete = SET_NULL, null=True)
    fk_id_usuario = models.ForeignKey(User, on_delete = SET_NULL, null=True)

    def __str__(self):
        return self.nombre_finca
