from django.contrib import admin
from .models import Carrera, Alumno, Evento, Inscripcion

admin.site.register(Carrera)
admin.site.register(Alumno)
admin.site.register(Evento)
admin.site.register(Inscripcion)
