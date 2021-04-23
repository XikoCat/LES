from django.db import models
from mains.models import Proponente
from Evento.models import TipoDeEvento, Evento
from Inscri�ao.models import Inscri��o, Feedback



class Formulário(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo_de_eventoid = models.ForeignKey('TipoDeEvento', models.SET_NULL, default=None, null=True, db_column='Tipo de eventoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_de_formulárioid = models.ForeignKey('TipoDeFormulário', models.SET_NULL, default=None, null=True, db_column='Tipo de FormulárioID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publico = models.IntegerField(db_column='Publico')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Formulário'

class FormulárioPergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    formulárioid = models.OneToOneField(Formulário, models.SET_NULL, default=None, null=True, db_column='FormulárioID')  # Field name made lowercase.
    perguntaid = models.OneToOneField('Pergunta', models.SET_NULL, default=None, null=True, db_column='PerguntaID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Formulário_Pergunta'


class OpçãoDeResposta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    perguntaid = models.ForeignKey('Pergunta', models.SET_NULL, default=None, null=True, db_column='PerguntaID')  # Field name made lowercase.
    opção = models.CharField(db_column='Opção', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Opção de resposta'




class Pergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pergunta = models.CharField(db_column='Pergunta', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obrigatório = models.IntegerField(db_column='Obrigatório')  # Field name made lowercase.
    tipo_de_perguntaid = models.ForeignKey('TipoDePergunta', models.SET_NULL, default=None, null=True, db_column='Tipo de perguntaID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Pergunta'

class Resposta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    perguntaid = models.ForeignKey(Pergunta, models.SET_NULL, default=None, null=True, db_column='PerguntaID')  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.SET_NULL, default=None, null=True, db_column='EventoID')  # Field name made lowercase.
    inscriçãoid = models.ForeignKey(Inscrição, models.SET_NULL, default=None, null=True, db_column='InscriçãoID')  # Field name made lowercase.
    feedbackid = models.ForeignKey(Feedback, models.SET_NULL, default=None, null=True, db_column='FeedbackID')  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=2048, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Resposta'


class TipoDeFormulário(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de Formulário'

class TipoDePergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de pergunta'


