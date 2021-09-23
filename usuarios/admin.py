from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import Usuario


# Register your models here.
class UsuarioAdmin(UserAdmin):
    list_display = ('email','username', 'is_student', 'matricula', 'curso', 'carrera', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email','username',)
    readonly_fields=('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Usuario, UsuarioAdmin)
