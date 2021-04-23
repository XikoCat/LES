from django.shortcuts import render
from .models import Sala

def consultar_salas(request):
	return render(request, "main/consultar_salas.html", {'Sala' : Sala.objects.all})
