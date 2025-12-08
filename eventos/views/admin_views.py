from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.db.models import Count

from eventos.models import Alumno, Evento, Inscripcion


def es_admin(user):
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(es_admin)
def panel_admin(request):
    total_alumnos = Alumno.objects.count()
    total_eventos = Evento.objects.count()
    total_inscripciones = Inscripcion.objects.count()

    evento_popular = (
        Inscripcion.objects
        .values('evento__titulo')
        .annotate(total=Count('id'))
        .order_by('-total')
        .first()
    )

    context = {
        'total_alumnos': total_alumnos,
        'total_eventos': total_eventos,
        'total_inscripciones': total_inscripciones,
        'evento_popular': evento_popular,
    }

    return render(request, 'eventos/panel_admin.html', context)
