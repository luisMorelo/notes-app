from django.urls import path
from .views import NotesList

urlpatterns = [
    path('', NotesList.as_view() )
]