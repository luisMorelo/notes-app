from django.shortcuts import render
from .models import Notes
from .serializers import notesSerializers
from rest_framework import generics

#--------- Vistas vasadas en clase para el modelo notas ------

class NotesList(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers 