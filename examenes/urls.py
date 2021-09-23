from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path(r'', views.ExamenesListView, name='examenes_list'),
    path(r'(?P<examen_id>[0-9]+)/$', views.RenderExamenView, name='detail'),
    path(r'solucion_examen/', views.CheckExamenView, name='check_examen'),
]
