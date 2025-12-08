from django.contrib import admin
from eventos.models import Carrera, Alumno, Evento, Inscripcion


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'carrera')
    search_fields = ('user__username',)
    list_filter = ('carrera',)


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'fecha',
        'hora_inicio',
        'hora_fin',
    )
    list_filter = ('fecha',)
    search_fields = ('titulo',)


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'evento', 'fecha_inscripcion')
    list_filter = ('evento',)
    search_fields = ('alumno__user__username',)
