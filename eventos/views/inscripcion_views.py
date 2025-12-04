from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date

from eventos.models import Inscripcion, Evento, Alumno


@login_required
def inscribir_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    alumno = Alumno.objects.filter(user=request.user).first()

    if not alumno:
        messages.error(request, "Tu usuario no está asociado a un alumno.")
        return redirect('evento_detalle', evento_id=evento_id)

    try:
        Inscripcion.objects.create(alumno=alumno, evento=evento)
        messages.success(request, "Inscripción realizada correctamente.")
    except Exception as e:
        messages.error(request, f"No se pudo inscribir: {str(e)}")

    return redirect('evento_detalle', evento_id=evento_id)


@login_required
def cancelar_inscripcion(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    alumno = Alumno.objects.filter(user=request.user).first()

    inscripcion = Inscripcion.objects.filter(alumno=alumno, evento=evento).first()

    if not inscripcion:
        messages.error(request, "No estás inscrito en este evento.")
        return redirect('evento_detalle', evento_id=evento_id)

    # No cancelar el mismo día o después
    if evento.fecha <= date.today():
        messages.error(request, "No puedes cancelar el día del evento o después.")
        return redirect('evento_detalle', evento_id=evento_id)

    inscripcion.delete()
    messages.success(request, "Inscripción cancelada correctamente.")
    return redirect('evento_detalle', evento_id=evento_id)
