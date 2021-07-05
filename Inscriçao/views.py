from Utilizadores.form import user_form
from django.core.checks import messages
from django.db.models.query_utils import Q
from Formulario.models import Formulário
from django.db.models.deletion import SET_NULL
from django.shortcuts import render, get_object_or_404, redirect

from .models import Inscrição, Pagamento
from Evento.models import Evento
from Utilizadores.models import Participante

from Formulario.forms import *

# Create your views here.

# Visualizar incrição de utilizadores no evento por evento
def consultar_inscricoes_evento(request, evento_id):
    evento = SET_NULL
    if evento_id != "all":
        if Evento.objects.filter(id=evento_id).exists():
            evento = Evento.objects.get(id=evento_id)
            return render(
                request,
                "consultar_inscricoes.html",
                {
                    "Inscrição": Inscrição.objects.all().filter(eventoid=evento),
                    "evento": evento,
                    "Dividas": Pagamento.objects.all,
                },
            )
        else:
            message = "Evento invalido"
            return render(request, "remover_inscricao.html", {"message": message})
    return render(
        request,
        "consultar_inscricoes.html",
        {
            "Inscrição": Inscrição.objects.all,
            "evento": evento,
            "Dividas": Pagamento.objects.all,
        },
    )

# Visualizar incrição de utilizadores no evento por user
def consultar_inscricoes_user(request, user_id):
    if Participante.objects.filter(utilizadorid=user_id).exists():
        user = Participante.objects.get(utilizadorid=user_id)
    else:
        message = "User invalido"
        return render(request, "remover_inscricao.html", {"message": message})
    return render(
        request,
        "consultar_inscricoes.html",
        {
            "Inscrição": Inscrição.objects.all().filter(participanteutilizadorid=user),
            "user": user,
            "Dividas": Pagamento.objects.all,
        },
    )


# Visualizar todas as inscrições en todos os eventos
def consultar_inscricoes_all(request):
    return redirect("/Inscricao/consultar_inscricoes_evento/all")


def querydict_to_dict(query_dict):
    data = {}
    for key in query_dict.keys():
        v = query_dict.getlist(key)
        if len(v) == 1:
            v = v[0]
        data[key] = v
    return data


# Visualizar todas as inscrições en todos os eventos
def criar_inscricao(request, evento_id):

    utilizador_id = request.user

    user = Participante.objects.get(utilizadorid=utilizador_id)

    if Inscrição.objects.filter(participanteutilizadorid=user).exists():
        message = "Este utilizador já se encontra inscrito"
        return render(
            request,
            "criar_inscricao.html",
            {"message": message, "user_id": utilizador_id},
        )

    evento = get_object_or_404(Evento, id=evento_id)
    tipo_form_inscricao = get_object_or_404(TipoDeFormulário, id=1)
    formulario = get_object_or_404(
        Formulário, evento_id=evento, tipo_de_formulárioid=tipo_form_inscricao
    )

    perguntas_list = FormulárioPergunta.objects.all().filter(formulárioid=formulario)

    if request.method != "POST":
        perguntas = []
        for p in perguntas_list:
            pergunta_tipo = p.perguntaid.tipo_de_perguntaid.id
            pergunta_max_choices = None
            pergunta_opcoes = []
            pergunta_length = None

            if pergunta_tipo == 1:
                pergunta_max_choices = p.perguntaid.numero_maximo_de_escolhas
                opcoes = OpçãoDeResposta.objects.all().filter(perguntaid=p.perguntaid)

                for o in opcoes:
                    pergunta_opcoes.append(o.opção)

            if pergunta_tipo == 2:
                pergunta_length = 16

            if pergunta_tipo == 3:
                pergunta_length = 128

            if pergunta_tipo == 4:
                pergunta_length = 512

            template = {
                "str": p.perguntaid.pergunta,
                "required": p.perguntaid.obrigatório,
                "type": pergunta_tipo,
                "max_choices": pergunta_max_choices,
                "answer_options": pergunta_opcoes,
                "answer_length": pergunta_length,
            }
            perguntas.append(template)

        return render(
            request,
            "criar_inscricao.html",
            {"formulario": formulario, "perguntas": perguntas},
        )
    else:

        Inscrição(
            eventoid=evento, participanteutilizadorid=user, checkin=False, valido=False
        ).save()
        inscricao = Inscrição.objects.get(
            eventoid=evento, participanteutilizadorid=user, checkin=False, valido=False
        )

        post = querydict_to_dict(request.POST)

        for p in perguntas_list:
            pergunta = p.perguntaid

            if pergunta.pergunta in post:
                answer = post[pergunta.pergunta]
                if isinstance(answer, list):
                    for a in answer:
                        Resposta(
                            perguntaid=pergunta,
                            eventoid=evento,
                            inscriçãoid=inscricao,
                            resposta=a,
                        ).save()
                else:
                    Resposta(
                        perguntaid=pergunta,
                        eventoid=evento,
                        inscriçãoid=inscricao,
                        resposta=answer,
                    ).save()

        message = "Inscrição criada com sucesso!!"
        return render(request, "criar_inscricao.html", {"message": message})


def remover_inscricao(request, inscricao_id):

    if not Inscrição.objects.filter(id=inscricao_id).exists():
        message = "A Inscrição que pretende remover não existe"
        return render(request, "remover_inscricao.html", {"message": message})

    inscricao = Inscrição.objects.get(id=inscricao_id)
    if request.method != "POST":
        return render(request, "remover_inscricao.html", {"inscricao": inscricao})
    else:
        Resposta.objects.filter(inscriçãoid=inscricao).delete()
        inscricao.delete()

        message = "A Inscrição foi removida com sucesso"
        return render(request, "remover_inscricao.html", {"message": message})
