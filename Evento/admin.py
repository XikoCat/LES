from django.contrib import admin
from Evento.models import *


admin.site.register(Evento)
admin.site.register(TipoDeEvento)
admin.site.register(PedidoDeRecurso)

admin.site.register(EventoLocais)
admin.site.register(EventoEquipamentos)
admin.site.register(EventoServicos)