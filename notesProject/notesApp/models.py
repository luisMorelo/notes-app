from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    version = models.PositiveIntegerField(default=0)  # Campo de versión para el bloqueo optimista

    def __str__(self):
        return self.titulo