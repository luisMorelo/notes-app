from rest_framework import serializers
from .models import Notes

class notesSerializers():
    class Meta: 
        model = Notes

        fields = ['titulo', 'contenido', 'fecha']

        #le indico que este campo sera solo lectura y no se puede modificar
        read_only_fields = ('fecha_creacion',) 