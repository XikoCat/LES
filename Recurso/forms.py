from django import forms
from django.forms import ModelForm
from .models import Evento


#Add an event
class evento_form(ModelForm):
	class Meta:
		model = Evento
		fields = ('tipo_de_eventoid', 'nome', 'estado', 'descrição', 'data', 'hora', 'duração', 'local', 'valor', 'evento_pagoid')

		widgets = {
			'tipo_de_eventoid' : forms.Select(attrs={'class' : 'form-control'}),
			'nome' : forms.TextInput(attrs={'class' : 'form-control'}),
			'estado' : forms.TextInput(attrs={'class' : 'form-control'}),
			'descrição' : forms.TextInput(attrs={'class' : 'form-control'}),
			'data' : forms.DateInput(attrs={'class' : 'form-control'}),
			'hora' : forms.TimeInput(attrs={'class' : 'form-control'}),
			'duração' : forms.TextInput(attrs={'class' : 'form-control'}),
			'local' : forms.TextInput(attrs={'class' : 'form-control'}),
			'valor' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'evento_pagoid' : forms.NumberInput(attrs={'class' : 'form-control'}),
		}