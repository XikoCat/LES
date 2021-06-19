from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, response
from .models import *
from Evento.models import *
from .forms import *


def consultar_perguntas(request):
	return render(request, "consultar_perguntas.html", {'Pergunta' : Pergunta.objects.all, 'OpcaoResposta' : OpçãoDeResposta.objects.all})

#def consultar_perguntas(request):
#	return render(request, "consultar_perguntas.html", {'Pergunta' : Pergunta.objects.all})
    
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


def remover_pergunta(request, pergunta_id):
    Pergunta_view = Pergunta.objects.get(pk = pergunta_id)
    Pergunta_view.delete()
    return redirect("Formulario:consultar_perguntas")

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

def editar_pergunta(request, pergunta_id):
    pergunta_edit = Pergunta.objects.get(pk = pergunta_id)
    p_form = pergunta_form(request.POST or None, instance=pergunta_edit)
    if p_form.is_valid():
        p_form.save()
        if pergunta_edit.tipo_de_perguntaid.id == 1:
            return redirect(f'/Formulario/add_opcao_resposta/{pergunta_edit.id}')
        return HttpResponseRedirect('/Formulario/add_pergunta?submitted=True')
    return render(request, "editar_pergunta.html", {'pergunta_edit': pergunta_edit, 'p_form':p_form})

def editar_opcao_resposta(request, pergunta_id, resposta_id):
    pergunta = get_object_or_404(Pergunta, id = pergunta_id)
    resposta = OpçãoDeResposta.objects.get(pk = resposta_id)
    respostas = OpçãoDeResposta.objects.all().filter(perguntaid = pergunta_id)
    respostaid = resposta.id
    form = opcao_resposta_form(request.POST or None, instance = resposta)
    if request.method == "POST":
        if form.is_valid(): 
            form.save()
            return redirect(f'/Formulario/add_opcao_resposta/{pergunta.id}')
    return render(request, "editar_add_opcao_resposta.html", {'pergunta' : pergunta, 'respostas' : respostas ,'form' : form , 'rid' : respostaid})




def consultar_formularios(request):
	return render(request, "consultar_formularios.html", {'Formulario' : Formulário.objects.all,})


def add_formularios(request):
    if request.method == "POST":
        form = novo_formulario_form(request.POST)
        if form.is_valid():
            new_form = Formulário(
                tipo_de_eventoid = get_object_or_404(TipoDeEvento, id = form.data['tipo_de_eventoid']),
                tipo_de_formulárioid = get_object_or_404(TipoDeFormulário,id = form.data['tipo_de_formulárioid']),
                nome = form.data['nome'],
                publico = True)
            new_form.save()
            return HttpResponseRedirect('/Formulario/add_pergunta?submitted=True')
    else:
        form = novo_formulario_form
    return render(request, "add_formulario.html", {'form' : form})

def add_formulario(request):
    if request.method == "POST":
        form = novo_formulario_form(request.POST)
        if form.is_valid():
            if form.data['tipo_de_formulárioid'] == get_object_or_404('tipo_de_formulárioid', nome = 'Proposta de evento'):
                form_2 = novo_formulario_form_2
                form_2.data = form.data
                return render(request, "add_formulario.html", {'form' : form})
            else:
                new_form = Formulário(
                tipo_de_eventoid = get_object_or_404(TipoDeEvento, id = form.data['tipo_de_eventoid']),
                tipo_de_formulárioid = get_object_or_404(TipoDeFormulário,id = form.data['tipo_de_formulárioid']),
                nome = form.data['nome'],
                publico = True)
                new_form.save()
            return HttpResponseRedirect('/Formulario/add_pergunta?submitted=True')

    else:
        form = novo_formulario_form
    return render(request, "add_formulario.html", {'form' : form})
