from django.urls import path
from .views import AlumnoRegisterView, ProfesorRegisterView, ProfileView


urlpatterns = [
    path('alumno/signup/', AlumnoRegisterView, name='alumno-signup'),
    path('profesor/signup/', ProfesorRegisterView, name='profesor-signup'),
    path('profile/', ProfileView, name='profile')
]
