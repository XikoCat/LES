from django import forms
from django.forms import ModelForm
from .models import Evento, PedidoDeRecurso


#Add an event
class evento_form(ModelForm):
	class Meta:
		model = Evento
		fields = ('tipo_de_eventoid', 'nome', 'descrição', 'data', 'hora', 'duração', 'locais', 'valor', 'evento_pagoid')

		labels = {
            'tipo_de_eventoid': ('Tipo de Evento'),
        }

		widgets = {
			'tipo_de_eventoid' : forms.Select(attrs={'class' : 'form-control'}),
			'nome' : forms.TextInput(attrs={'class' : 'form-control'}),
			'descrição' : forms.TextInput(attrs={'class' : 'form-control'}),
			'data' : forms.DateInput(attrs={'class' : 'form-control'}),
			'hora' : forms.TimeInput(attrs={'class' : 'form-control'}),
			'duração' : forms.TextInput(attrs={'class' : 'form-control'}),
			'local' : forms.TextInput(attrs={'class' : 'form-control'}),
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

