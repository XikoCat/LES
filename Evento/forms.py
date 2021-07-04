from django import forms
from django.forms import ModelForm
from .models import *


#Add an event
class evento_form(ModelForm):
	class Meta:
		model = Evento
		fields = ('tipo_de_eventoid', 'nome', 'descrição', 'data', 'hora', 'duração', 'valor', 'evento_pagoid')

		labels = {
            'tipo_de_eventoid': ('Tipo de Evento'),
        }

		widgets = {
			'tipo_de_eventoid' : forms.Select(attrs={'class' : 'form-control'}),
			'nome' : forms.TextInput(attrs={'class' : 'form-control'}),
			'descrição' : forms.TextInput(attrs={'class' : 'form-control'}),
			'data' : forms.DateInput(attrs={'class' : 'form-control'}),
			'hora' : forms.TimeInput(attrs={'class' : 'form-control'}),
			'duração' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'valor' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'evento_pagoid' : forms.NumberInput(attrs={'class' : 'form-control'}),
		}

#Add logistic
class logistica_form(ModelForm):
	class Meta:
		model = PedidoDeRecurso
		fields = ('eventoid', 'tipo_de_recursoid', 'quantidade', 'dia_inicial', 'hora_inicial','dia_final'
				 ,'hora_final', 'capacidade')

		labels = {
            'eventoid': ('Evento'),
            'tipo_de_recursoid': ('Tipo de Recurso'),
            'quantidade': ('Quantidade desejada'),
        }

		widgets = {
			'eventoid' : forms.Select(attrs={'class' : 'form-control'}),
			'tipo_de_recursoid' : forms.Select(attrs={'class' : 'form-control'}),
			'quantidade' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'dia_inicial' : forms.DateInput(attrs={'class' : 'form-control'}),
			'dia_final' : forms.DateInput(attrs={'class' : 'form-control'}),
			'hora_inicial' : forms.TimeInput(attrs={'class' : 'form-control'}),
			'hora_final' : forms.TimeInput(attrs={'class' : 'form-control'}),
			'capacidade' : forms.NumberInput(attrs={'class' : 'form-control'}),
		}

class atribuir_sala_form(ModelForm):
	class Meta:
		model = EventoLocais
		fields = ('localId', )

class atribuir_equipamento_form(ModelForm):
	class Meta:
		model = EventoEquipamentos
		fields = ('equipamentoId', )

class atribuir_serviço_form(ModelForm):
	class Meta:
		model = EventoServicos
		fields = ('servicoId', )