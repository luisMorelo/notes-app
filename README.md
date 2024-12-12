Instrucciones sobre cómo configurar y ejecutar el proyecto localmente


## Instalación
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