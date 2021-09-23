from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Examen, ExamenResuelto

admin.site.register(Examen)
admin.site.register(ExamenResuelto)
