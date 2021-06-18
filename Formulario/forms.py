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
            'tipo_de_formulárioid',
            'tipo_de_eventoid',
            
        )
        labels = {
            'tipo_de_formulárioid': ('Tipo de formulário'),
            'tipo_de_eventoid': ('Tipo de evento'),
            
        }

    def __init__(self,data = None, *args, **kwargs):
        super(novo_formulario_form, self).__init__(data, *args, **kwargs)
        if data and data.get('tipo_de_formulárioid', None) == self. 