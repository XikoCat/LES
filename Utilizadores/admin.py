from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class Admin(UserAdmin):
	list_display = ('email','username','nome','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Administrador)
admin.site.register(Participante)
admin.site.register(Proponente)
admin.site.register(Utilizador, Admin)