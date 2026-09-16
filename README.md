# CFT San Agustín — Sistema de Eventos

![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django) ![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python) ![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-336791?logo=postgresql) ![Bootstrap](https://img.shields.io/badge/UI-Bootstrap-7952B3?logo=bootstrap)

Sistema web para que los alumnos del CFT San Agustín se inscriban a eventos y actividades del instituto, y para que administración gestione la oferta de eventos y consulte estadísticas de participación.

## Qué resuelve

Coordinar inscripciones a charlas, talleres y actividades por planilla o WhatsApp no escala: se pierde el control de cupos y es fácil que un alumno quede inscrito en dos eventos que se superponen en horario. Este sistema centraliza la inscripción, valida cupos y choques de horario automáticamente, y le da a cada rol (alumno / administrador) su propio panel.

## Features

- **Catálogo de eventos** público con fecha, horario y cupos.
- **Inscripción a eventos** con dos validaciones automáticas al guardar:
  - No se puede inscribir si el evento ya alcanzó su `cupo_maximo`.
  - No se puede inscribir a dos eventos que se superponen en fecha y horario.
- **Cancelación de inscripción**.
- **Login con roles** y redirección automática al dashboard correspondiente:
  - **Panel alumno** — sus inscripciones.
  - **Panel administrador** — total de alumnos, eventos e inscripciones, y el evento más popular (ranking por cantidad de inscritos).
- Gestión de carreras y alumnos vía el admin nativo de Django.

## Stack

- Django 6.0 + Python
- PostgreSQL (`psycopg`)
- Bootstrap (templates Django, sin frontend separado)

## Arquitectura

```
cftSanAgustin_eventos/      # settings, urls, wsgi/asgi del proyecto
eventos/
├── models.py               # Carrera, Alumno, Evento, Inscripcion
├── views/
│   ├── home_views.py
│   ├── evento_views.py     # listado y detalle (calcula cupos disponibles)
│   ├── inscripcion_views.py
│   ├── auth_views.py       # redirect_dashboard(): deriva por rol (staff -> admin, Alumno -> alumno)
│   ├── alumno_views.py     # panel_alumno
│   └── admin_views.py      # panel_admin (solo staff/superuser), metricas agregadas
├── templates/eventos/      # base.html (Bootstrap) + una plantilla por vista
└── static/eventos/         # logos e imágenes
```

### Modelo de datos

```python
Carrera        # nombre
Alumno         # 1:1 con User, rut, carrera
Evento         # titulo, descripcion, fecha, hora_inicio, hora_fin, cupo_maximo
Inscripcion    # alumno + evento (unique_together), valida cupos y choque de horario en .clean()
```

La validación de cupos y de choque de horario vive en `Inscripcion.clean()` y se ejecuta en cada `save()`, así que aplica sin importar desde dónde se cree la inscripción (vista, admin o shell).

## Puesta en marcha local

1. Crear entorno virtual e instalar dependencias:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   pip install -r requirements.txt
   ```
2. Crear la base de datos PostgreSQL y configurar las credenciales (ver sección Configuración).
3. Aplicar migraciones y cargar un usuario administrador:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Levantar el servidor:
   ```bash
   python manage.py runserver
   ```
   o en Windows: `runserver.bat`

## Configuración

`cftSanAgustin_eventos/settings.py` trae hoy la configuración de base de datos, `SECRET_KEY` y `DEBUG` **hardcodeadas** para desarrollo local. Antes de desplegar este proyecto o de subir cambios a `settings.py`, mover estos valores a variables de entorno (`django-environ` o `python-decouple`) y **rotar tanto la contraseña de PostgreSQL como el `SECRET_KEY`**, ya que los valores actuales están expuestos en el historial del repositorio.

```env
DJANGO_SECRET_KEY=...
DJANGO_DEBUG=False
DB_NAME=cftSanAgustin_eventos_db
DB_USER=postgres
DB_PASSWORD=...
DB_HOST=localhost
DB_PORT=5432
```

## Autor

**Iván Solís Manqueo** — Full Stack Developer, Talca, Chile
[iasmtech.com](https://iasmtech.com) · [ivan.solis20.m@gmail.com](mailto:ivan.solis20.m@gmail.com)
