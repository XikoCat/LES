from django.shortcuts import render
from Pergunta.models import Evento

# Create your views here.

def consultar_eventos(request):
	context = {
		"Eventos" : Evento.objects.all,
	}
	return render(request, "consultar_eventos.html", context)