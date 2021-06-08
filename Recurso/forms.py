from django.forms import ModelForm
from .models import *

class salas_form(ModelForm):
    class Meta:
        model = Sala
        fields = ('edificioid', 'lugares')
        
class edificios_form(ModelForm):
    class Meta:
        model = Edificio
        fields = ('id', 'campusid', 'nome',)
        
class campus_form(ModelForm):
    class Meta:
        model = Campus
        fields = ('nome', 'morada')
        
class recursos_form(ModelForm):
    class Meta:
        model = Recurso
        fields = ('nome', 'estado')