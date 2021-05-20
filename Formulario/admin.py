from django.contrib import admin
from Formulario.models import Pergunta
from Formulario.models import Formulário
from Formulario.models import TipoDePergunta

admin.site.register(Pergunta)
admin.site.register(Formulário)
admin.site.register(TipoDePergunta)
