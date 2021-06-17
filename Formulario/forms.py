from django import forms
from django.forms import ModelForm, fields, widgets
from .models import *

class pergunta_form(ModelForm):
    class Meta:
        model = Pergunta
        fields = (
            'pergunta',
            'obrigatório',
            'tipo_de_perguntaid'
        )

        labels = {
            'tipo_de_perguntaid': ('Tipo de pergunta')
        }

class opcao_resposta_form(ModelForm):
    class Meta:
        model = OpçãoDeResposta
        fields = (
            'opção',
        )

        labels = {
            'opção': ('Resposta'),
        }

class novo_formulario_form(ModelForm):
    class Meta:
        model = Formulário
        fields = (
            'nome',
            'tipo_de_eventoid',
            'tipo_de_formulárioid'
        )
        labels = {
            'tipo_de_eventoid': ('Tipo de evento'),
            'tipo_de_formulárioid': ('Tipo de formulário'),
        }