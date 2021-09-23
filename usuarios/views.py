import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from usuarios.forms import AlumnoRegistrationForm, ProfesorRegistrationForm
from usuarios.models import Usuario
from examenes.models import ExamenResuelto

logger = logging.getLogger('django_info')


def AlumnoRegisterView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = AlumnoRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['form'] = form

    else:
        form = AlumnoRegistrationForm()
        context['form'] = form
    return render(request, 'signup.html', context)

def ProfileView(request, *args, **kwargs):
    user = request.user
    # Pendientes sacar los examenes, quizzes y tareas
    if user.is_authenticated:
        examenes = ExamenResuelto.objects.filter(numero_cuenta=user.matricula, curso=user.curso)
        return render(request, 'usuarios/profile.html', {"user":user, "examenes": examenes})
    else:
        return redirect('home')


def ProfesorRegisterView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = ProfesorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            """
            # Create a SuperUser
            su = Usuario.objects.get(email="miguel.eva.alv@gmail.com")
            if su:
                su.is_admin = True
                su.is_staff = True
                su.is_superuser = True
                su.save()
                logger.info("SU Created")
            """
            return redirect('home')
        else:
            context['form'] = form

    else:
        form = ProfesorRegistrationForm()
        context['form'] = form
    return render(request, 'signup.html', context)
