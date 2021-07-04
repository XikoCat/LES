import Formulario
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, response
from .models import *
from Evento.models import *
from .forms import *


def consultar_perguntas(request, id, formulario_id):
    opções = OpçãoDeResposta.objects.all()
    perguntas = Pergunta.objects.all().filter(temporario=False)
    if formulario_id != str(None):
        formulario_perguntas = FormulárioPergunta.objects.all().filter(
            formulárioid=formulario_id
        )
        for f in formulario_perguntas:
            perguntas = perguntas.all().exclude(id=f.perguntaid.id)
    return render(
        request,
        "consultar_perguntas.html",
        {
            "id": id,
            "formulario_id": formulario_id,
            "Pergunta": perguntas,
            "OpcaoResposta": opções,
        },
    )


def add_pergunta(request, formulario_id):
    submitted = False
    if request.method == "POST":
        form = pergunta_form(request.POST)
        if form.is_valid():
            pergunta = form.save()
            if pergunta.tipo_de_perguntaid.id == 1:
                return redirect(
                    f"/Formulario/add_opcao_resposta/{pergunta.id}/{formulario_id}" 
                )
            return HttpResponseRedirect(
                f"/Formulario/add_pergunta/{formulario_id}?submitted=True"
            )
    else:
        form = pergunta_form
        if "submitted" in request.GET:
            submitted = True
    return render(
        request,
        "add_pergunta.html",
        {"form": form, "formulario_id": formulario_id, "submitted": submitted},
    )


def remover_pergunta(request, pergunta_id, formulario_id):
    Pergunta_view = Pergunta.objects.get(pk=pergunta_id)
    Pergunta_view.delete()
    if(formulario_id == "None"):
        url = f"/Formulario/consultar_perguntas/0/{formulario_id}"
    else:
        url = f"/Formulario/consultar_perguntas/1/{formulario_id}" 
    return redirect(url)


def add_opcao_resposta(request, pergunta_id, formulario_id):
    pergunta = get_object_or_404(Pergunta, id=pergunta_id)
    respostas = OpçãoDeResposta.objects.all().filter(perguntaid=pergunta_id)
    if request.method == "POST":
        form = opcao_resposta_form(request.POST)
        if form.is_valid():
            query = OpçãoDeResposta(perguntaid=pergunta, opção=form.data["opção"])
            query.save()
    else:
        form = opcao_resposta_form
    state = False
    if pergunta.temporario == True:
        state = True
    return render(
        request,
        "add_opcao_resposta.html",
        {
            "pergunta": pergunta,
            "formulario_id": formulario_id,
            "respostas": respostas,
            "form": form,
            "state": state,
        },
    )


def delete_resposta(request, pergunta_id, resposta_id, formulario_id):
    query = OpçãoDeResposta.objects.get(pk=resposta_id)
    query.delete()
    return redirect(f"/Formulario/add_opcao_resposta/{pergunta_id}/{formulario_id}")


def editar_pergunta(request, pergunta_id, formulario_id):
    submitted = False
    pergunta_edit = Pergunta.objects.get(pk=pergunta_id)
    p_form = pergunta_form(request.POST or None, instance=pergunta_edit)
    state = False
    if request.method == "POST":
        if p_form.is_valid():
            p_form.save()
            if pergunta_edit.tipo_de_perguntaid.id == 1:
                return redirect(
                    f"/Formulario/add_opcao_resposta/{pergunta_edit.id}/{formulario_id}"
                )
            return HttpResponseRedirect(
                f"/Formulario/editar_pergunta/{pergunta_edit.id}/{formulario_id}?submitted=True"
            )
    else:
        if "submitted" in request.GET:
            submitted = True
    if(pergunta_edit.temporario == True):
        state = True
    return render(
        request,
        "editar_pergunta.html",
        {
            "pergunta_edit": pergunta_edit,
            "formulario_id": formulario_id,
            "p_form": p_form,
            "state": state,
            "submitted": submitted
        },
    )


def editar_opcao_resposta(request, pergunta_id, resposta_id, formulario_id):
    pergunta = get_object_or_404(Pergunta, id=pergunta_id)
    resposta = OpçãoDeResposta.objects.get(pk=resposta_id)
    respostas = OpçãoDeResposta.objects.all().filter(perguntaid=pergunta_id)
    respostaid = resposta.id
    form = opcao_resposta_form(request.POST or None, instance=resposta)
    state = False
    if(pergunta.temporario == True):
        state = True
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(
                f"/Formulario/add_opcao_resposta/{pergunta.id}/{formulario_id}"
            )
    return render(
        request,
        "editar_add_opcao_resposta.html",
        {
            "pergunta": pergunta,
            "formulario_id": formulario_id,
            "respostas": respostas,
            "form": form,
            "rid": respostaid,
            "state": state,
        },
    )


def consultar_formularios(request):
    return render(
        request,
        "consultar_formularios.html",
        {
            "Formulario": Formulário.objects.all,
        },
    )


def add_formulario(request):
    if request.method == "POST":
        form = novo_formulario_form(request.POST)
        if form.is_valid():
            if form.data["tipo_de_eventoid"] != "":
                new_form = Formulário(
                    tipo_de_eventoid=get_object_or_404(
                        TipoDeEvento, id=form.data["tipo_de_eventoid"]
                    ),
                    tipo_de_formulárioid=get_object_or_404(
                        TipoDeFormulário, id=form.data["tipo_de_formulárioid"]
                    ),
                    nome=form.data["nome"],
                    publico=False,
                )
            else:
                new_form = Formulário(
                    tipo_de_formulárioid=get_object_or_404(
                        TipoDeFormulário, id=form.data["tipo_de_formulárioid"]
                    ),
                    nome=form.data["nome"],
                    publico=False,
                )
            new_form.save()
            return redirect(f"/Formulario/add_pergunta_ao_formulario/{new_form.id}")
    else:
        form = novo_formulario_form
    state = False
    return render(request, "add_formulario.html", {"form": form, "state": state})


def add_pergunta_ao_formulario(request, formulario_id):
    formulario = Formulário.objects.get(pk=formulario_id)
    perguntas_id = FormulárioPergunta.objects.all().filter(formulárioid=formulario)
    perguntas = []
    for p in perguntas_id:
        perguntas.append(p.perguntaid)
    return render(
        request,
        "add_pergunta_ao_formulario.html",
        {
            "formulario": formulario,
            "perguntas": perguntas,
            "OpcaoResposta": OpçãoDeResposta.objects.all,
        },
    )


def eliminar_formulario(request, formulario_id):
    Formulario_view = Formulário.objects.get(pk=formulario_id)
    formulario_pergunta = FormulárioPergunta.objects.all().filter(
        formulárioid=Formulario_view
    )
    for fv in formulario_pergunta:
        pergunta = Pergunta.objects.get(pk=fv.perguntaid.id)
        if pergunta.temporario == True:
            pergunta.delete()
    Formulario_view.delete()

    return redirect("Formulario:consultar_formularios")


def editar_formulario(request, formulario_id):
    formulario_edit = Formulário.objects.get(pk=formulario_id)
    form = novo_formulario_form(request.POST or None, instance=formulario_edit)
    if form.is_valid():
        form.save()
        return redirect(f"/Formulario/add_pergunta_ao_formulario/{formulario_edit.id}")
    state = True
    return render(request, "add_formulario.html", {"form": form, "state": state})


def alterar_estado_formulario(request, formulario_id):
    formulario_edit = Formulário.objects.get(pk=formulario_id)
    formulario_edit.publico = not formulario_edit.publico
    formulario_edit.save()
    return redirect(f"/Formulario/consultar_formularios")


def add_pergunta_ao_formulario_action(request, pergunta_id, formulario_id):
    pergunta_add = FormulárioPergunta(
        formulárioid=get_object_or_404(Formulário, id=formulario_id),
        perguntaid=get_object_or_404(Pergunta, id=pergunta_id),
    )
    pergunta_add.save()
    return redirect(f"/Formulario/consultar_perguntas/{1}/{formulario_id}")


def remover_pergunta_do_formulario(request, pergunta_id, formulario_id):
    formulario = Formulário.objects.get(pk=formulario_id)
    pergunta = Pergunta.objects.get(pk=pergunta_id)
    formulario_pergunta = FormulárioPergunta.objects.get(
        formulárioid=formulario, perguntaid=pergunta
    )
    formulario_pergunta.delete()
    if pergunta.temporario == True:
        pergunta.delete()
    return redirect(f"/Formulario/add_pergunta_ao_formulario/{formulario_id}")


def editar_pergunta_do_formulario(request, pergunta_id, formulario_id):
    submitted = False
    pergunta_edit = Pergunta.objects.get(pk=pergunta_id)
    p_form = pergunta_form(request.POST or None, instance=pergunta_edit)
    state = True
    if request.method == "POST":
        if p_form.is_valid():
            if pergunta_edit.temporario == False:
                obr = request.POST.get('obrigatório', pergunta_edit.obrigatório)      
                formulario_pergunta = FormulárioPergunta.objects.get(perguntaid=pergunta_id)
                formulario_pergunta.delete()
                new_pergunta = Pergunta(
                    pergunta = p_form.data["pergunta"],
                    obrigatório = obr,
                    tipo_de_perguntaid=get_object_or_404(
                        TipoDePergunta, id=p_form.data["tipo_de_perguntaid"]
                    ),
                    temporario=True,
                )
                new_pergunta.pk = None

                if new_pergunta.obrigatório == "on":
                    new_pergunta.obrigatório = True
                else:
                    new_pergunta.obrigatório = False

                new_pergunta.save()
                new_formulario_pergunta = FormulárioPergunta(
                    formulárioid=get_object_or_404(Formulário, id=formulario_id),
                    perguntaid=get_object_or_404(Pergunta, id=new_pergunta.id),
                )

                new_formulario_pergunta.pk = None
                new_formulario_pergunta.save()

                opções = OpçãoDeResposta.objects.all().filter(perguntaid=pergunta_edit)
                for o in opções:
                    new_opção = OpçãoDeResposta(perguntaid=new_pergunta, opção=o.opção)
                    new_opção.pk = None
                    new_opção.save()

                if new_pergunta.tipo_de_perguntaid.id == 1:
                    return redirect(
                        f"/Formulario/add_opcao_resposta/{new_pergunta.id}/{formulario_id}"
                    )
                return HttpResponseRedirect(
                    f"/Formulario/editar_pergunta_do_formulario/{new_pergunta.id}/{formulario_id}?submitted=True"
                )
            else:
                p_form.save()
                if pergunta_edit.tipo_de_perguntaid.id == 1:
                    return redirect(
                        f"/Formulario/add_opcao_resposta/{pergunta_id}/{formulario_id}"
                    )
                return HttpResponseRedirect(
                    f"/Formulario/editar_pergunta_do_formulario/{pergunta_id}/{formulario_id}?submitted=True"
                )
    else:
        if "submitted" in request.GET:
            submitted = True
    return render(
        request,
        "editar_pergunta.html",
        {
            "pergunta_edit": pergunta_edit,
            "formulario_id": formulario_id,
            "p_form": p_form,
            "state": state,
            "submitted": submitted
        },
    )