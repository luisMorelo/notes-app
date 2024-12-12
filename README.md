Instrucciones sobre cómo configurar y ejecutar el proyecto localmente


## Instalación
1. Clona el repositorio así: 

    git clone https://github.com/luisMorelo/notes-app.git

2. Crea y activa un entorno virtua:

    Crear un entorno virtual con: python -m venv venv

    Activar el entorno virtual con:

    ■ Windows: .venv\Scripts\activate
    ■ Unix/Linux: source venv/bin/activate


3. Instalar dependencias así: pip install -r requirements.txt

4. Realiza migraciones a la base de datos:

    python manage.py makemigrations 

    python manage.py migrate

5. Ejecuta el servidor de desarrollo

    python manage.py runserver
    


### instrucciones sobre cómo configurar la conexión a la base de datos.Base de Datos (PostgreSQL):

- Crear la base de datos y el usuario necesarios.

- Crear la base de datos y el usuario necesarios.

- Variables de Entorno
    Configura la siguiente variable de entorno en tu archivo `.env.example` o en tu entorno de ejecución:

    DB_PASSWORD=   #Escribe allí la contraseña de tu base de datos postgret

