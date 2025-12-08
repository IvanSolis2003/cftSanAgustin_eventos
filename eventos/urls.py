from django.urls import path

from .views.home_views import home
from .views.evento_views import eventos_lista, evento_detalle
from .views.inscripcion_views import inscribir_evento, cancelar_inscripcion
from .views.auth_views import redirect_dashboard
from .views.alumno_views import panel_alumno
from .views.admin_views import panel_admin


urlpatterns = [
    path('', home, name='home'),

    # Eventos
    path('eventos/', eventos_lista, name='eventos_lista'),
    path('evento/<int:evento_id>/', evento_detalle, name='evento_detalle'),
    path('inscribir/<int:evento_id>/', inscribir_evento, name='inscribir_evento'),
    path('cancelar/<int:evento_id>/', cancelar_inscripcion, name='cancelar_inscripcion'),

    # Dashboard por rol
    path('dashboard/', redirect_dashboard, name='dashboard'),

    # Panel alumno
    path('panel/alumno/', panel_alumno, name='alumno_dashboard'),

    # Panel administrador
    path('panel/admin/', panel_admin, name='admin_dashboard'),
]
