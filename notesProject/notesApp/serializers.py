from rest_framework import serializers
from .models import Notes, User
from rest_framework.serializers import ModelSerializer

class notesSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Notes

        fields = ['titulo', 'contenido', 'fecha_creacion']

        #le indico que este campo sera solo lectura y no se puede modificar
        
        read_only_fields = ('fecha_creacion',) 


# Serializador para el modelo User
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Campos necesarios para el registro
        extra_kwargs = {
            'password': {'write_only': True}  # Para que el password no se muestre en la respuesta
        }

    def create(self, validated_data):
        # Crear un usuario con contraseña cifrada
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user