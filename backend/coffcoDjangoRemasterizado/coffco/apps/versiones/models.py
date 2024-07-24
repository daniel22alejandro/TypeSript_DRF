from django.db import models
from django.db.models import SET_NULL
from apps.tipo_formato.models import TipoFormato
from apps.users.models import User
from apps.documentos.models import Documentos



class Versiones(models.Model):
    version = models.CharField(max_length=45)
    editable = models.BooleanField()
    fk_id_tipo_formato = models.ForeignKey(TipoFormato, on_delete = SET_NULL, null=True)
    fk_id_usuarios = models.ForeignKey(User, on_delete = SET_NULL, null=True)
    formato_vacio = models.BinaryField(null=True)
    fk_documentos = models.ForeignKey(Documentos, on_delete = SET_NULL, null=True)

    def __str__(self):
        return self.version
