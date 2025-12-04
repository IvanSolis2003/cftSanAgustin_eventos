from django.shortcuts import render, get_object_or_404
from .models import Evento, Alumno, Inscripcion

def eventos_lista(request):
    eventos = Evento.objects.order_by('fecha', 'hora_inicio')
    return render(request, 'eventos/eventos_lista.html', {'eventos': eventos})


def evento_detalle(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    inscrito = False
    if request.user.is_authenticated:
        alumno = Alumno.objects.filter(user=request.user).first()
        if alumno:
            inscrito = Inscripcion.objects.filter(alumno=alumno, evento=evento).exists()

    return render(request, 'eventos/evento_detalle.html', {
        'evento': evento,
        'inscrito': inscrito
    })
