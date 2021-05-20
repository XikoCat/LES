from django.shortcuts import render
from .models import Pergunta
from django.shortcuts import redirect

def consultar_perguntas(request):
	return render(request, "consultar_perguntas.html", {'Pergunta' : Pergunta.objects.all})

#def consultar_perguntas(request):
#	return render(request, "consultar_perguntas.html", {'Pergunta' : Pergunta.objects.all})

def remover_pergunta(request, pergunta_id):
    Pergunta_view = Pergunta.objects.get(pk = pergunta_id)
    Pergunta_view.delete()
    return redirect("Formulario:consultar_perguntas")
