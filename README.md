

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