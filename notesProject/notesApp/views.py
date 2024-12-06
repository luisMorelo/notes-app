from django.shortcuts import render
from .models import Notes
from .serializers import notesSerializers
from rest_framework import generics

#--------- Vistas vasadas en clase para el modelo notas ------

#Para listar notas
class NotesList(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers 

#para crear notas
class NotesCreate(generics.CreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers

#ver un objeto unico pot ID
class TaskDetail(generics.RetrieveAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers

#Actualizar notas
class TaskUpdate(generics.UpdateAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers

#Borar un registro 
class TaskDelete(generics.DestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers