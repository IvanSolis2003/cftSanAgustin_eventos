from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date

from eventos.models import Alumno, Inscripcion


@login_required
def panel_alumno(request):
    alumno = Alumno.objects.filter(user=request.user).first()

    if not alumno:
        # Seguridad: si no es alumno, vuelve al home
        return render(request, 'eventos/home.html')

    inscripciones = Inscripcion.objects.filter(alumno=alumno).select_related('evento')

    eventos_futuros = []
    eventos_pasados = []

    for ins in inscripciones:
        if ins.evento.fecha >= date.today():
            eventos_futuros.append(ins)
        else:
            eventos_pasados.append(ins)

    context = {
        'eventos_futuros': eventos_futuros,
        'eventos_pasados': eventos_pasados,
    }

    return render(request, 'eventos/panel_alumno.html', context)
