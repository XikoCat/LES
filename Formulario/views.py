from django.shortcuts import render
from django.http import HttpResponse
from .models import Pergunta

def consultar_perguntas(request):
	return render(request, "main/consultar_perguntas.html", {'Pergunta' : Pergunta.objects.all})
