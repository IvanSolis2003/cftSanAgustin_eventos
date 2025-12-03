from django.db import models
from django.contrib.auth.models import User


class Carrera(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cupo_maximo = models.PositiveIntegerField(default=20)

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"


class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('alumno', 'evento')

    def __str__(self):
        return f"{self.alumno} inscrito en {self.evento}"

    # --- VALIDACIONES ---
    def clean(self):
        from django.core.exceptions import ValidationError

        # 1) Validar cupos
        inscritos = Inscripcion.objects.filter(evento=self.evento).count()
        if inscritos >= self.evento.cupo_maximo:
            raise ValidationError("El evento ya no tiene cupos disponibles.")

        # 2) Validar choque de horario
        otros = Inscripcion.objects.filter(alumno=self.alumno)

        for ins in otros:
            if ins.evento.fecha == self.evento.fecha:
                choca = not (
                    self.evento.hora_fin <= ins.evento.hora_inicio or
                    self.evento.hora_inicio >= ins.evento.hora_fin
                )
                if choca:
                    raise ValidationError("Tienes otro evento inscrito en el mismo horario.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
