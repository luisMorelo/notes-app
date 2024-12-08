from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .serializers import notesSerializers
from rest_framework import generics, permissions
from .forms import SingUpForm, LoginForms, NotesForm
from django.contrib.auth import login, authenticate, logout
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




# Función para registrarse
def user_signup(request):
    if request.method == 'GET':
        form = SingUpForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():  # Verifica que los datos sean válidos
            user = form.save()  # Crea el usuario con los datos del formulario
            login(request, user)  # Inicia sesión automáticamente al usuario
            return render(request, 'register.html', {'form': form, 'exito': '¡El usuario fue creado exitosamente!'})
        else:
            return render(request, 'register.html', {'form': form, 'error': form.errors }) #¡Datos inválidos! Cree una contraseña segura que tenga mínimo 8 caracteres, incluyendo letras, números y símbolos



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
    

#Lista de notas y dashboart
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
            print('Nota creada con éxito')
            return redirect('dashboard')
        except ValueError:
            print("Formulario inválido", form.errors)  # Imprime los errores del formulario
            return render(request, 'crear-nota.html', {"form": form, "error": "Error al crear nota."})


#Editar nota
@login_required
def editar_nota(request, nota_id):
    nota = get_object_or_404(Notes, id=nota_id, user=request.user)
    
    if request.method == "GET":
        form = NotesForm(instance=nota)
        return render(request, 'editar-notas.html', {"form": form, "nota": nota})
    else:
        try:
            form = NotesForm(request.POST, instance=nota)
            form.save()
            return redirect('dashboard')
        except ValueError:
            return render(request, 'editar-notas.html', {"form": form, "nota": nota, "error": "Error al editar la nota."})



#Eliminar tarea
def eliminar_nota(request, nota_id):
    nota = get_object_or_404(Notes, id=nota_id)
    if request.method == "POST":
        nota.delete()
        return redirect('dashboard')  # redirige a la lista de tareas después de eliminar

    return render(request, 'eliminar-nota.html', {'nota': nota})


#cerrar sesion
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar-sesion')