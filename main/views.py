from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento
from .models import Pergunta
from .models import Sala

# Create your views here.
def homepage(request):
	return render(request = request, template_name = "main/home.html", context = {"Eventos": Evento.objects.all})
	

def consultar_eventos(request):
	context = {
		"Eventos" : Evento.objects.all,
	}
	return render(request, "main/consultar_eventos.html", context)

def consultar_perguntas(request):
	return render(request, "main/consultar_perguntas.html", {'Pergunta' : Pergunta.objects.all})

def consultar_salas(request):
	return render(request, "main/consultar_salas.html", {'Sala' : Sala.objects.all})
