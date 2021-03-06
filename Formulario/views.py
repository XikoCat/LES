import Formulario
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, response
from .models import *
from Evento.models import *
from .forms import *
from Inscriçao.views import querydict_to_dict


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


def consultar_formularios(request, evento_id):
    evento = get_object_or_404(Evento, id = evento_id)
    formularios = Formulário.objects.all().filter(evento_id = evento)
    state = 'evento'
    return render(
        request,
        "consultar_formularios.html",
        {
            "Formulario": formularios,
            "evento":evento,
            "state":state
        },
    )

def consultar_formularios_special(request):
    formularios = Formulário.objects.all().filter(
        tipo_de_formulárioid = get_object_or_404(
            TipoDeFormulário, nome = 'Proposta de evento'))
    state = 'false'
    return render(
        request,
        "consultar_formularios.html",
        {
            "Formulario": formularios,
            "state":state,
        },
    )

def add_formulario(request, evento_id):
    state = False
    if request.method == "POST":
        form = novo_formulario_form(request.POST)
        if form.is_valid():
            if Formulário.objects.filter(
                evento_id = evento_id,
                tipo_de_formulárioid=get_object_or_404(
                        TipoDeFormulário,
                        id=form.data["tipo_de_formulárioid"]
                    )
                ).exists():
                message = "Este tipo de formulario já existe para este evento!"
                return render(request, "add_formulario.html", {"form": form, "state": state, "evento_id": evento_id, "error_message": message})

            if get_object_or_404(TipoDeFormulário, id = form.data["tipo_de_formulárioid"]) !=  get_object_or_404(TipoDeFormulário, nome = "Proposta de evento"):
                new_form = Formulário(
                    tipo_de_formulárioid=get_object_or_404(
                        TipoDeFormulário, id=form.data["tipo_de_formulárioid"]
                    ),
                    nome=form.data["nome"],
                    publico=False,
                    evento_id=get_object_or_404(
                        Evento, id= evento_id
                    ),
                )
            else:
                if Formulário.objects.filter(
                    tipo_de_eventoid=get_object_or_404(
                        TipoDeEvento,id=form.data["tipo_de_eventoid"])
                    ).exists():
                    message = "Já existe um formulário para propor eventos para este tipo de evento!"
                    return render(request, "add_formulario.html", {"form": form, "state": state, "evento_id": evento_id, "error_message": message})

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
            new_form.save()
            return redirect(f"/Formulario/add_pergunta_ao_formulario/{new_form.id}")
    else:
        form = novo_formulario_form
    return render(request, "add_formulario.html", {"form": form, "state": state, "evento_id": evento_id})

def add_formulario_special(request):
    state = False
    if request.method == "POST":
        form = novo_formulario_2_form(request.POST)
        if form.is_valid():
            if Formulário.objects.filter(
                tipo_de_eventoid=get_object_or_404(
                        TipoDeEvento,
                        id=form.data["tipo_de_eventoid"]
                    )
                ).exists():
                message = "Já existe um formulário para propor eventos para este tipo de evento!"
                return render(request, "add_formulario_special.html", {"form": form, "state": state, "error_message": message})

            new_form = Formulário(
                tipo_de_eventoid=get_object_or_404(
                    TipoDeEvento, id=form.data["tipo_de_eventoid"]),
                tipo_de_formulárioid=get_object_or_404(
                    TipoDeFormulário, nome= 'Proposta de evento'),
                nome=form.data["nome"],
                publico=False,  
            )
            new_form.save()
            return redirect(f"/Formulario/add_pergunta_ao_formulario/{new_form.id}")
    else:
        form = novo_formulario_2_form
    return render(request, "add_formulario_special.html", {"form": form, "state": state})


def add_pergunta_ao_formulario(request, formulario_id):
    formulario = Formulário.objects.get(pk=formulario_id)
    perguntas_id = FormulárioPergunta.objects.all().filter(formulárioid=formulario).order_by('pos')
    count = len(FormulárioPergunta.objects.all().filter(formulárioid = formulario_id))

    perguntas = []
    for p in perguntas_id:
        perguntas.append(p.perguntaid)

    evento_id = None
    if formulario.evento_id !=None : 
        evento_id = formulario.evento_id.id

    return render(
        request,
        "add_pergunta_ao_formulario.html",
        {
            "formulario": formulario,
            "perguntas": perguntas_id,
            "OpcaoResposta": OpçãoDeResposta.objects.all,
            "count": count,
            "evento_id":evento_id
        },
    )

def pergunta_move_up(request, pergunta_id, formulario_id):
    formulario = Formulário.objects.get(pk=formulario_id)
    pergunta = Pergunta.objects.get(pk=pergunta_id)
    pergunta_form = FormulárioPergunta.objects.get(
        formulárioid = formulario, perguntaid=pergunta)

    other_pergunta_form = FormulárioPergunta.objects.get(
        formulárioid = formulario, pos = pergunta_form.pos-1)

    other_pergunta_form.pos += 1
    pergunta_form.pos -= 1
    other_pergunta_form.save()
    pergunta_form.save()
    return redirect(f"/Formulario/add_pergunta_ao_formulario/{formulario.id}")


def pergunta_move_down(request, pergunta_id, formulario_id):
    formulario = Formulário.objects.get(pk=formulario_id)
    pergunta = Pergunta.objects.get(pk=pergunta_id)
    pergunta_form = FormulárioPergunta.objects.get(
        formulárioid = formulario, perguntaid=pergunta)

    other_pergunta_form = FormulárioPergunta.objects.get(
        formulárioid = formulario, pos = pergunta_form.pos+1)

    other_pergunta_form.pos -= 1
    pergunta_form.pos += 1
    other_pergunta_form.save()
    pergunta_form.save()
    return redirect(f"/Formulario/add_pergunta_ao_formulario/{formulario.id}")

def eliminar_formulario(request, formulario_id):
    Formulario_view = Formulário.objects.get(pk=formulario_id)
    formulario_pergunta = FormulárioPergunta.objects.all().filter(
        formulárioid=Formulario_view
    )
    for fv in formulario_pergunta:
        pergunta = Pergunta.objects.get(pk=fv.perguntaid.id)
        if pergunta.temporario == True:
            pergunta.delete()
    if Formulario_view.evento_id !=None :
        Formulario_view.delete() 
        return redirect(f"/Formulario/consultar_formularios/{Formulario_view.evento_id.id}" )
    Formulario_view.delete()
    return redirect(f"/Formulario/consultar_formularios_special" )


def editar_formulario(request, formulario_id):
    formulario_edit = Formulário.objects.get(pk=formulario_id)
    tipo_de_formulario = formulario_edit.tipo_de_formulárioid
    form = novo_formulario_form(request.POST or None, instance=formulario_edit)
    state = True

    if form.is_valid():
        formulario_edit2 = Formulário.objects.filter(
            evento_id = formulario_edit.evento_id,
            tipo_de_formulárioid=get_object_or_404(
                    TipoDeFormulário,
                    id=form.data["tipo_de_formulárioid"]
                )
            )

        if get_object_or_404(TipoDeFormulário, id = form.data["tipo_de_formulárioid"]) !=  get_object_or_404(TipoDeFormulário, nome = "Proposta de evento"):
            if get_object_or_404(TipoDeFormulário, id=form.data["tipo_de_formulárioid"]) == tipo_de_formulario:
                form.save()
                return redirect(f"/Formulario/add_pergunta_ao_formulario/{formulario_edit.id}")
            elif formulario_edit2.exists():
                message = "Este tipo de formulario já existe para este evento!"
                return render(request, "add_formulario.html", {"form": form, "state": state, "evento_id": formulario_edit.evento_id.id, "error_message": message})
        
        else:
            formulario_edit2 = Formulário.objects.filter(
            tipo_de_eventoid=get_object_or_404(
                    TipoDeEvento,
                    id=form.data["tipo_de_eventoid"]
                )
            )
            if formulario_edit2.exists():
                message = "Já existe um formulário para propor eventos para este tipo de evento!"
                return render(request, "add_formulario.html", {"form": form, "state": state, "evento_id": formulario_edit.evento_id.id, "error_message": message})
            formulario_edit.delete()
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
            new_form.save()
            return redirect(f"/Formulario/add_pergunta_ao_formulario/{new_form.id}")
        form.save()
        return redirect(f"/Formulario/add_pergunta_ao_formulario/{formulario_edit.id}")
    return render(request, "add_formulario.html", {"form": form, "state": state, "evento_id": formulario_edit.evento_id.id}) 


def editar_formulario_special(request, formulario_id):
    state = True
    formulario_edit = Formulário.objects.get(pk=formulario_id)
    tipo_de_evento = formulario_edit.tipo_de_eventoid
    form = novo_formulario_2_form(request.POST or None, instance=formulario_edit)
    if form.is_valid():
        formulario_edit2 = Formulário.objects.filter(
            tipo_de_eventoid=get_object_or_404(
                    TipoDeEvento,
                    id=form.data["tipo_de_eventoid"]
                )
            )
        if get_object_or_404(TipoDeEvento, id=form.data["tipo_de_eventoid"]) == tipo_de_evento:
            form.save()
            return redirect(f"/Formulario/add_pergunta_ao_formulario/{formulario_edit.id}")

        elif formulario_edit2.exists():
            message = "Já existe um formulário para propor eventos para este tipo de evento!"
            return render(request, "add_formulario_special.html", {"form": form, "state": state, "error_message": message})

        form.save()
        return redirect(f"/Formulario/add_pergunta_ao_formulario/{formulario_edit.id}")
    return render(request, "add_formulario_special.html", {"form": form, "state": state})


def alterar_estado_formulario(request, formulario_id):
    formulario_edit = Formulário.objects.get(pk=formulario_id)
    formulario_edit.publico = not formulario_edit.publico
    formulario_edit.save()
    if formulario_edit.evento_id !=None :
        return redirect(f"/Formulario/consultar_formularios/{formulario_edit.evento_id.id}" )
    return redirect(f"/Formulario/consultar_formularios_special" )


def add_pergunta_ao_formulario_action(request, pergunta_id, formulario_id):
    count = len(FormulárioPergunta.objects.all().filter(formulárioid = formulario_id))
    pergunta_add = FormulárioPergunta(
        formulárioid=get_object_or_404(Formulário, id=formulario_id),
        perguntaid=get_object_or_404(Pergunta, id=pergunta_id),
        pos=count+1
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
    formulario =get_object_or_404(Formulário, id=formulario_id)
    p_form = pergunta_form(request.POST or None, instance=pergunta_edit)
    state = True
    if request.method == "POST":
        if p_form.is_valid():
            if pergunta_edit.temporario == False:
                obr = request.POST.get('obrigatório', pergunta_edit.obrigatório)      
                formulario_pergunta = FormulárioPergunta.objects.all().filter( perguntaid = pergunta_edit, formulárioid = formulario)
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
                for fp in formulario_pergunta:
                    new_formulario_pergunta = FormulárioPergunta(
                        formulárioid=get_object_or_404(Formulário, id=formulario_id),
                        perguntaid=get_object_or_404(Pergunta, id=new_pergunta.id),
                        pos = fp.pos , 
                    )
                formulario_pergunta.delete()

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