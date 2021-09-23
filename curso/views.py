from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import AuthenticationForm


def home(request):
    response = render(request, 'home.html', {"is_home": True})
    return response

def credits(request):
    response = render(request, 'misc/credits.html')
    return response

def biblio(request):
    response = render(request, 'misc/biblio.html')
    return response

def sesiones(request):
    response = render(request, 'misc/sesiones.html')
    return response

def _logout(request):
    logout(request)
    return redirect("home")

def _login(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    context = {}
    if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            print("ENTRE HASTA AQUI")
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
    context['form'] = form
    return render(request, "login.html", context)

# Define error templates
def bad_request(request, exception=None):
    response = render(request, 'errors/400.html')
    response.status_code = 400
    return response


def permission_denied(request, exception=None):
    response = render(request, 'errors/403.html')
    response.status_code = 403
    return response


def page_not_found(request, exception=None):
    response = render(request, 'errors/404.html')
    response.status_code = 404
    return response


def server_error(request, exception=None):
    response = render(request, 'errors/500.html')
    response.status_code = 500
    return response
