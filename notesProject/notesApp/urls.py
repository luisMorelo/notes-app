from django.urls import path
from .import views 

urlpatterns = [
    path('put/api/notes', views.NotesCreate.as_view()),
    path('get/api/notes', views.NotesList.as_view())
]