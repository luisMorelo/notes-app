from django.shortcuts import render, redirect
from .models import Notes
from .serializers import notesSerializers
from rest_framework import generics, permissions
from .forms import SingUpForm, LoginForms, NotesForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#--------- Vistas vasadas en clase para el modelo notas ------

#Para listar notas
class NotesList(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers 
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación
    
#para crear notas
class NotesCreate(generics.CreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

#ver un objeto unico pot ID
class NotesDetail(generics.RetrieveAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

#Actualizar notas
class NotesUpdate(generics.UpdateAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

#Borar un registro 
class NotesDelete(generics.DestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = notesSerializers
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación




#Función para registrarse
def user_signup(request):

    form = SingUpForm()
    if request.method == 'GET':
        return render(request,'register.html', {
            'form': form
        })
    else:
        if request.method == 'POST':

            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1']
                )
                user.save()
                login(request, user)
                
                return render(request, 'register.html', {'form': form, 'exito': '¡El usuario fue creado exitósamente!'})
            else:
                return render(request, 'register.html', {'form': form, 'error': 'Las contraseñas no coinciden, verifica e intentalo de nuevo'})




#Función para iniciar sesión
def user_login(request):
    if request.method == 'GET':
        form = LoginForms()
        return render(request, 'login.html', {"form": form})
    else:
        form = LoginForms(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {"form": form, "error": "El usuario o la contraseña son incorrectos"})
        else:
            return render(request, 'login.html', {"form": form, "error": "Por favor, corrija los errores del formulario"})
    

#Lista de tareas y dashboart
@login_required
def dashboard(request):
    notes = Notes.objects.filter(user=request.user)
    return render(request, 'index.html', { 'notes': notes })


#Crear una nueva tarea
@login_required
def crear_nota(request):

    form = NotesForm()

    if request.method == "GET":
        return render(request, 'crear-nota.html', {"form": form})
    else:
        try:
            form = NotesForm(request.POST)
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()
            return redirect('dashboard')
        except ValueError:
            return render(request, 'crear-nota.html', {"form": form, "error": "Error al crear nota."})
