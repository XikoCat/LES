from django.contrib import admin
from .models import Administrador, Participante, Proponente, Utilizador
# Register your models here.

admin.site.register(Administrador)
admin.site.register(Participante)
admin.site.register(Proponente)
admin.site.register(Utilizador)
