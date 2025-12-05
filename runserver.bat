@echo off
cd /d %~dp0

REM Activar entorno virtual
call venv\Scripts\activate

REM Ejecutar migraciones
echo Ejecutando makemigrations...
python manage.py makemigrations
echo Ejecutando migrate...
python manage.py migrate

REM Crear superusuario en modo interactivo
echo Ahora se ejecuta createsuperuser (completa usuario, email y contraseña)...
python manage.py createsuperuser

REM Levantar servidor de desarrollo
echo Levantando servidor Django...
python manage.py runserver

pause