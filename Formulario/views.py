from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, response
from .models import *
from .forms import *


def consultar_perguntas(request):
	return render(request, "consultar_perguntas.html", {'Pergunta' : Pergunta.objects.all, 'OpcaoResposta' : OpçãoDeResposta.objects.all})

#def consultar_perguntas(request):
#	return render(request, "consultar_perguntas.html", {'Pergunta' : Pergunta.objects.all})

def remover_pergunta(request, pergunta_id):
    Pergunta_view = Pergunta.objects.get(pk = pergunta_id)
    Pergunta_view.delete()
    return redirect("Formulario:consultar_perguntas")

    
def add_pergunta(request):
    submitted = False 
    if request.method == "POST":
        form = pergunta_form(request.POST)
        if form.is_valid():
            pergunta = form.save()
            if pergunta.tipo_de_perguntaid.id == 1:
                return redirect(f'/Formulario/add_opcao_resposta/{pergunta.id}')
            return HttpResponseRedirect('/Formulario/add_pergunta?submitted=True')
    else:
        form = pergunta_form
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "add_pergunta.html", {'form' : form, 'submitted' : submitted})

def add_opcao_resposta(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, id = pergunta_id)
    respostas = OpçãoDeResposta.objects.all().filter(perguntaid = pergunta_id)
    if request.method == "POST":
        form = opcao_resposta_form(request.POST)
        if form.is_valid():
            query = OpçãoDeResposta(perguntaid = pergunta, opção = form.data['opção'])
            query.save()
    else:
        form = opcao_resposta_form
    return render(request, "add_opcao_resposta.html", {'pergunta' : pergunta, 'respostas' : respostas ,'form' : form})

def delete_resposta(request, pergunta_id ,resposta_id):
    query = OpçãoDeResposta.objects.get(pk = resposta_id)
    query.delete()
    return redirect(f'/Formulario/add_opcao_resposta/{pergunta_id}')