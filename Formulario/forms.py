from django import forms
from django.forms import ModelForm, fields, widgets
from .models import *
from django.shortcuts import get_object_or_404

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

        widgets = {
			'pergunta' : forms.TextInput(attrs={'class' : 'form-control'}),
            'tipo_de_perguntaid' : forms.Select(attrs={'class' : 'form-control'}),
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

        widgets = {
			'opção' : forms.TextInput(attrs={'class' : 'form-control'}),
		}
        
class novo_formulario_form(ModelForm):

    class Meta:
        model = Formulário
        tipo_de_eventoid = forms.CharField(required=True)
        fields = (
            'nome',
            'tipo_de_formulárioid',
            'tipo_de_eventoid',
        )
        labels = {
            'tipo_de_formulárioid': ('Tipo de formulário'),
            'tipo_de_eventoid': ('Tipo de evento'),
        }

        widgets = {
			'nome' : forms.TextInput(attrs={'class' : 'form-control'}),
            'tipo_de_formulárioid' : forms.Select(attrs={'class' : 'form-control'}),
            'tipo_de_eventoid' : forms.Select(attrs={'class' : 'form-control'}),
		}

class novo_formulario_2_form(ModelForm):

    class Meta:
        model = Formulário
        tipo_de_eventoid = forms.CharField(required=True)
        fields = (
            'nome',
            'tipo_de_eventoid',
        )
        labels = {
            'tipo_de_eventoid': ('Tipo de evento'),
        }

        widgets = {
			'nome' : forms.TextInput(attrs={'class' : 'form-control'}),
            'tipo_de_eventoid' : forms.Select(attrs={'class' : 'form-control'}),
		}