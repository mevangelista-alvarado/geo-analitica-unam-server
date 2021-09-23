from django.conf import settings
from django.db import models
from django.utils import timezone
from .questions_info import QUESTIONS

class Examen(models.Model):
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CURSE_CHOICES = [
        (0, "2022-1")
    ]
    curso = models.IntegerField(choices=CURSE_CHOICES, default=0)
    tema = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)
    pregunta1 = models.IntegerField(choices=QUESTIONS, default=0)
    pregunta2 = models.IntegerField(choices=QUESTIONS, default=0)
    pregunta3 = models.IntegerField(choices=QUESTIONS, default=0)
    pregunta4 = models.IntegerField(choices=QUESTIONS, default=0)
    pregunta5 = models.IntegerField(choices=QUESTIONS, default=0)
    activo = models.BooleanField(default=True)
    is_test = models.BooleanField(default=False)

class ExamenResuelto(models.Model):
    examen_id = models.TextField(blank=True, max_length=100, default="")
    curso = models.TextField(blank=True, max_length=100, default="")
    numero_cuenta = models.TextField(blank=True, max_length=100, default="")
    tema = models.TextField(blank=True, max_length=100, default="")
    tiempo = models.TextField(blank=True, max_length=100, default="")
    calificacion = models.TextField(blank=True, max_length=10, default="")
    pregunta1 = models.TextField(blank=True, max_length=10000, default="")
    respuesta1_correcta = models.TextField(blank=True, max_length=10000, default="")
    respuesta1_alumno = models.TextField(blank=True, max_length=10000, default="")
    respuesta1_calif = models.TextField(blank=True, max_length=10000, default="")
    pregunta2 = models.TextField(blank=True, max_length=10000, default="")
    respuesta2_correcta = models.TextField(blank=True, max_length=10000, default="")
    respuesta2_alumno = models.TextField(blank=True, max_length=10000, default="")
    respuesta2_calif = models.TextField(blank=True, max_length=10000, default="")
    pregunta3 = models.TextField(blank=True, max_length=10000, default="")
    respuesta3_correcta = models.TextField(blank=True, max_length=10000, default="")
    respuesta3_alumno = models.TextField(blank=True, max_length=10000, default="")
    respuesta3_calif = models.TextField(blank=True, max_length=10000, default="")
    pregunta4 = models.TextField(blank=True, max_length=10000, default="")
    respuesta4_correcta = models.TextField(blank=True, max_length=10000, default="")
    respuesta4_alumno = models.TextField(blank=True, max_length=10000, default="")
    respuesta4_calif = models.TextField(blank=True, max_length=10000, default="")
    pregunta5 = models.TextField(blank=True, max_length=10000, default="")
    respuesta5_correcta = models.TextField(blank=True, max_length=10000, default="")
    respuesta5_alumno = models.TextField(blank=True, max_length=10000, default="")
    respuesta5_calif = models.TextField(blank=True, max_length=10000, default="")
