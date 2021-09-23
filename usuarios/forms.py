from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from usuarios.models import Usuario


class AlumnoRegistrationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'username', 'nombre', 'password1', 'password2', 'matricula', 'curso', 'carrera', 'is_student']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'pedro.gomez@tudominio.com'}),
            'username': forms.TextInput(attrs={'placeholder': 'Elige un alias'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Pedro Goméz'}),
            'matricula': forms.TextInput(attrs={'placeholder': 'Cuenta UNAM'}),
            'is_student': forms.HiddenInput(),
        }

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if '@ciencias.unam.mx' not in email:
            raise forms.ValidationError('El email: {} NO es una cuenta @ciencias.unam.mx, por favor usa una.'.format(email))
        try:
            account = Usuario.objects.exclude(pk=self.instance.pk).get(email=email)
        except Usuario.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Usuario.objects.exclude(pk=self.instance.pk).get(username=username)
        except Usuario.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


class ProfesorRegistrationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'username', 'nombre', 'password1', 'password2', 'curso', 'is_student']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'pedro.gomez@tudominio.com'}),
            'username': forms.TextInput(attrs={'placeholder': 'Elige un alias'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Pedro Goméz'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Usuario.objects.exclude(pk=self.instance.pk).get(email=email)
        except Usuario.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Usuario.objects.exclude(pk=self.instance.pk).get(username=username)
        except Usuario.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)
