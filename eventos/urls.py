from django.urls import path
from .views.home_views import home
from .views.evento_views import eventos_lista, evento_detalle
from .views.inscripcion_views import inscribir_evento, cancelar_inscripcion
from .views.auth_views import redirect_dashboard
from .views.alumno_views import panel_alumno


urlpatterns = [
    path('', home, name='home'),

    path('eventos/', eventos_lista, name='eventos_lista'),
    path('evento/<int:evento_id>/', evento_detalle, name='evento_detalle'),
    path('inscribir/<int:evento_id>/', inscribir_evento, name='inscribir_evento'),
    path('cancelar/<int:evento_id>/', cancelar_inscripcion, name='cancelar_inscripcion'),

    path('dashboard/', redirect_dashboard, name='dashboard'),

    path('panel/alumno/', panel_alumno, name='alumno_dashboard'),
    path('panel/admin/', home, name='admin_dashboard'),
]
