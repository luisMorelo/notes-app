

## Instrucciones sobre cómo configurar y ejecutar el proyecto localmente

Instalación
Requisitos previos:
Asegúrate de tener instalado Python 3.8 o superior y Git.

1. Clona el repositorio así: 

    git clone https://github.com/luisMorelo/notes-app.git

2. Crea y activa un entorno virtua:

    Crear un entorno virtual con: python -m venv venv

    Activar el entorno virtual con:

    ■ Windows: .venv\Scripts\activate
    ■ Unix/Linux: source venv/bin/activate


3. Instalar dependencias así: pip install -r requirements.txt


4. Base de Datos (PostgreSQL):
    Crear una base de datos con el nombre 'notes' desde PgAdmin.

    Variables de Entorno
        Configura la siguiente variable de entorno en el archivo `.env.example`

        DB_PASSWORD=   #Escriba la contraseña del usuario 'postgres' para conectarse al servidor - "PostgreSQL"


5. Realiza migraciones a la base de datos:

    python manage.py makemigrations 

    python manage.py migrate


5. Ejecuta el servidor de desarrollo

    python manage.py runserver

6. (opcional) Crear un usuario admin para gestioanr el modelo notas Django Admin
    
    python manage.py createsuperuser

    Este comando te pedirá que ingreses:

    Username: El nombre de usuario para tu administrador.
    Email address: Una dirección de correo electrónico válida.
    Password: Una contraseña segura.

    y listo, ya podrás acceder desde el localhost http://127.0.0.1:8000/admin con tus credenciales 


## Tecnologías utilizadas y razones para elegirlas.

- Backend
    Django:
        Razones:
        Framework web robusto y maduro para Python, ideal para desarrollar aplicaciones rápidamente.
        Ofrece un ORM potente (Object-Relational Mapper) que simplifica la interacción con la base de datos.
        Cuenta con una gran comunidad y una amplia gama de aplicaciones y librerías de terceros.
        Su enfoque "batteries included" proporciona muchas funcionalidades listas para usar, como el sistema de autenticación, el sistema de administración y el sistema de URL.

-Bootstrap:
    Razones:
        Como todava no he trabajo con Reac y typescript´me pareció una muy buna opcion para lo que se estaba pidiendo en la pueba técnica, es un Framework de front-end popular y ampliamente utilizado para construir interfaces de usuario responsivas y además proporciona una gran cantidad de componentes prediseñados (Como botones, formularios, tablas, etc.) que aceleran el desarrollo.


## Explicación detallada de la estrategia de bloqueo implementada.

- Estrategia de Bloqueo Optimista:
    
    El bloqueo optimista es una técnica que sirve para manejar concurrencia en aplicaciones donde múltiples usuarios o procesos pueden intentar modificar la misma información al mismo tiempo.

    El bloqueo optimista permite que múltiples usuarios trabajen simultáneamente, pero verifica que los datos no hayan cambiado antes de guardar los cambios.

    En este caso, se implementó el bloqueo optimista para evitar conflictos al editar notas desde diferentes pestañas. Esto asegura la integridad de los datos y evita sobrescribir cambios realizados en otra pestaña.

   
    1. Campo de versión (version):
    Cada registro en la base de datos tiene un campo version que se incrementa cada vez que el registro es modificado. Este campo se utiliza para detectar si el dato ha cambiado entre la lectura y el intento de escritura.

    2. Fecha de última modificación (updated_at):
    Aunque el campo updated_at no es esencial para el bloqueo optimista, se utiliza en el formulario para dar una referencia temporal y permitir validaciones adicionales en el cliente (JavaScript).

    Flujo de Trabajo

        Lectura del registro:
        Cuando el usuario accede a la página de edición, los datos actuales de la nota se cargan en el formulario, incluyendo el valor de version.

        Modificación concurrente:
        Otro usuario o proceso puede modificar la misma nota y guardar los cambios, incrementando el valor de version en la base de datos.

        Intento de guardado:
        Cuando el primer usuario intenta guardar los cambios:

        Se envía el valor de version almacenado en el formulario al servidor.
        El servidor compara el valor enviado con el valor actual en la base de datos.
        
        Validación del bloqueo:

        Éxito: Si el valor de version coincide, los cambios se guardan, y el campo version se incrementa en +1.
        Conflicto: Si los valores no coinciden, se rechaza la operación y se informa al usuario que la nota ha sido modificada en otra parte.


## Desafío enfrentado
-Primero entender claramente los conceptos de concurrencia para tener claridad sobre las condiciones de carrera, sobre las técnicas de bloqueo existentes y los casos donde estas se podían aplicar

-Implementar la técnica de bloqueo optimista: 
    Una vez tuve claro los conceptos, el reto fue tratar de implementar esta técnica mediante solicitudes AJAX con JavaScript que no me estaban funcionando, entonces luego cambié y adapté la vista de editar_nota que ya tenía en Python para que además de editar también hiciera esas validaciones y pudiera darle solución a lo que se estaba pidiendo. 
    Esta parte del proyecto fue la que me tomó mas tiempo, por lo que tuve que intentar de varias maneras como implementar la técnica con el front, pero al final lo logré y la satisfacción ¡fue única!