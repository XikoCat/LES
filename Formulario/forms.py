from django import forms
from django.forms import ModelForm, fields, widgets
from .models import OpçãoDeResposta, Pergunta

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