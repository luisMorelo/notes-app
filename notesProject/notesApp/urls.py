from django.urls import path
from .import views 
from rest_framework.authtoken.views import obtain_auth_token

#ENDPOINTS DE LA APLICACCIÓN
urlpatterns = [

    #ENDPOINTS DE AUTENTICACIÓN
    path('api/auth/register', views.UserCreate.as_view()), #Registrar un nuevo usuario.
    path('api/auth/login', obtain_auth_token, name='api_token_auth'), #Autenticar a un usuario y devolver un JWT.
    
    #ENDPOINTS DE NOTAS CON LA API
    path('get/api/notes', views.NotesList.as_view()), #Recuperar todas las notas para el usuario autenticado.
    path('put/api/notes', views.NotesCreate.as_view()),#Crear una nueva nota.
    path('get/api/notes/<int:nota_id>', views.NotesList.as_view()), #Recuperar una nota específica.
    path('PUT/api/notes/<int:nota_id>', views.NotesUpdate.as_view()), #Actualiza una nota específica
    path('DELETE/api/notes/<int:nota_id>', views.NotesDelete.as_view()), #Elimina una nota

    #ENDPOINT CON EL FRONTEND
    path('registro', views.user_signup, name='registro-usuario'), #Registrarse
    path('', views.user_login, name='iniciar-sesion'), #Iniciar sesión
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-notes/', views.crear_nota , name='crear-nota'),
    path('editar/<int:nota_id>/', views.editar_nota , name='editar-nota'),
    path('eliminar-nota/<int:nota_id>/', views.eliminar_nota , name='eliminar-nota'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar-sesion'),

    #ENDPOINT DE PRUEBA DE BLOQUEO OPTIMISTA DE CONCURRENCIA
   
]