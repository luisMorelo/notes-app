from django.urls import path
from .import views 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    path('put/api/notes', views.NotesCreate.as_view()),
    path('get/api/notes', views.NotesList.as_view()),
]