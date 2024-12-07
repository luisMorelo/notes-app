from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)  # La fecha cuando se actualiza

    def __str__(self):
        return self.titulo