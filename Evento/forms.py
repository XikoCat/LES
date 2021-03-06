from django import forms
from django.forms import ModelForm
from .models import *


#Add an event
class evento_form(ModelForm):
	class Meta:
		model = Evento
		fields = ('tipo_de_eventoid', 'nome', 'descrição', 'data', 'hora', 'duração', 'valor')

		labels = {
            'tipo_de_eventoid': ('Tipo de Evento'),
            'duração' : ('Duração em horas'),
            'valor' : ('Preço do evento em €')
        }

		widgets = {
			'tipo_de_eventoid' : forms.Select(attrs={'class' : 'form-control'}),
			'nome' : forms.TextInput(attrs={'class' : 'form-control'}),
			'descrição' : forms.TextInput(attrs={'class' : 'form-control'}),
			'data' : forms.DateInput(attrs={'class' : 'form-control'}),
			'hora' : forms.TimeInput(attrs={'class' : 'form-control'}),
			'duração' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'valor' : forms.NumberInput(attrs={'class' : 'form-control'}),
		}

#Add logistic
class logistica_form(ModelForm):
	class Meta:
		model = PedidoDeRecurso
		fields = ('tipo_de_recursoid', 'quantidade', 'dia_inicial', 'hora_inicial','dia_final'
				 ,'hora_final', 'capacidade')

		labels = {
            'tipo_de_recursoid': ('Tipo de Recurso'),
            'quantidade': ('Quantidade desejada'),
            'capacidade': ('Capacidade (caso seja uma sala)')
        }

		widgets = {
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

		widgets = {
			'localId' : forms.Select(attrs={'class' : 'form-control'}),
		}


class atribuir_equipamento_form(ModelForm):
	class Meta:
		model = EventoEquipamentos
		fields = ('equipamentoId', )

		widgets = {
			'equipamentoId' : forms.Select(attrs={'class' : 'form-control'}),
		}

class atribuir_serviço_form(ModelForm):
	class Meta:
		model = EventoServicos
		fields = ('servicoId', )

		widgets = {
			'servicoId' : forms.Select(attrs={'class' : 'form-control'}),
		}