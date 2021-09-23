"""curso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^logout/', views._logout, name='logout'),
    url(r'^login/', views._login, name='login'),
    url(r'^creditos/', views.credits, name='credits'),
    url(r'^bibliografia/', views.biblio, name='biblio'),
    url(r'^sesiones/', views.sesiones, name='sesiones'),
    # path('', include('examenes.urls')),
    path('usuario/', include('usuarios.urls')),
    path('examenes/', include('examenes.urls')),
]

# Manage Error requests
handler400 = 'curso.views.bad_request'
handler403 = 'curso.views.permission_denied'
handler404 = 'curso.views.page_not_found'
handler500 = 'curso.views.server_error'
