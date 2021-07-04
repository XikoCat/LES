from Formulario.models import Formulário
from django.db.models.deletion import SET_NULL
from django.shortcuts import render, get_object_or_404, redirect

from .models import Inscrição, Pagamento
from Evento.models import Evento

from Formulario.forms import *

# Create your views here.

# Visualizar incrição de utilizadores no evento
def consultar_inscricoes(request, evento_id):
    evento = SET_NULL
    if evento_id != "all":
        evento = get_object_or_404(Evento, id=evento_id)
    return render(
        request,
        "consultar_inscricoes.html",
        {
            "Inscrição": Inscrição.objects.all,
            "evento": evento,
            "Dividas": Pagamento.objects.all,
        },
    )


# Visualizar todas as inscrições en todos os eventos
def consultar_inscricoes_all(request):
    return redirect("/Inscricao/consultar_inscricoes/all")


# Visualizar todas as inscrições en todos os eventos
def criar_inscricao(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    tipo_form_inscricao = get_object_or_404(TipoDeFormulário, id=1)
    formulario = get_object_or_404(
        Formulário, evento_id=evento, tipo_de_formulárioid=tipo_form_inscricao
    )

    perguntas_list = FormulárioPergunta.objects.all().filter(formulárioid=formulario)
    print(len(perguntas_list))

    perguntas = []
    for p in perguntas_list:
        pergunta_str = p.perguntaid.pergunta
        pergunta_must = p.perguntaid.obrigatório
        pergunta_tipo = p.perguntaid.tipo_de_perguntaid.id

        #se pergunta tipo == 1
        pergunta_max_choices = p.perguntaid.numero_maximo_de_escolhas

        #se pergunta tipo == 2
        pergunta_length = 16

        #se pergunta tipo == 3
        pergunta_length = 128

        #se pergunta tipo == 4
        pergunta_length = 512

        template = {
            "str": pergunta_str,
            "must": pergunta_must,
            "type": pergunta_tipo,
            "max_choices": pergunta_max_choices,
            "resposta_length": pergunta_length
        }
        perguntas.append(template)

    # perguntas.append()

    return render(
        request,
        "criar_inscricao.html",
        {"formulario": formulario, "perguntas": perguntas},
    )
