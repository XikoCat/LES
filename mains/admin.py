from django.contrib import admin
from .models import Administrador
from .models import CertificadoDeParticipação
from .models import Evento
from .models import TipoDeEvento
from .models import Pergunta
from .models import TipoDePergunta
from .models import Sala
# Register your models here.

admin.site.register(Administrador)
admin.site.register(CertificadoDeParticipação)
admin.site.register(Evento)
admin.site.register(TipoDeEvento)
admin.site.register(Pergunta)
admin.site.register(TipoDePergunta)
admin.site.register(Sala)


