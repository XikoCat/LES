# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Administrador'


class Campus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Campus'


class CertificadoDeParticipação(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventoid = models.ForeignKey('Evento', models.SET_NULL, default=None, null=True, db_column='EventoID')  # Field name made lowercase.
    nome_evento = models.CharField(db_column='Nome evento', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_emissão = models.DateField(db_column='Data emissão', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nome_participante = models.CharField(db_column='Nome participante', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publico = models.IntegerField(db_column='Publico')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificado de Participação'


class Edificio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, models.SET_NULL, default=None, null=True, db_column='CampusID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Edificio'


class Equipamento(models.Model):
    recursoid = models.OneToOneField('Recurso', models.DO_NOTHING, db_column='RecursoID', primary_key=True)  # Field name made lowercase.
    tipo_de_equipamentoid = models.ForeignKey('TipoDeEquipamento', models.DO_NOTHING, db_column='Tipo de equipamentoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Equipamento'


class Evento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo_de_eventoid = models.ForeignKey('TipoDeEvento', models.SET_NULL, default=None, null=True, db_column='Tipo de eventoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    proponenteutilizadorid = models.ForeignKey('Proponente', models.SET_NULL, default=None, null=True, db_column='ProponenteUtilizadorID')  # Field name made lowercase.
    formulárioinscriçãoid = models.ForeignKey('Formulário', models.SET_NULL, default=None, null=True, db_column='FormulárioInscriçãoID')  # Field name made lowercase.
    formuláriofeedbackid = models.ForeignKey('Formulário', models.SET_NULL, default=None, null=True, related_name = 'feedback', db_column='FormulárioFeedbackID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descrição = models.CharField(db_column='Descrição', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    duração = models.IntegerField(db_column='Duração', blank=True, null=True)  # Field name made lowercase.
    local = models.IntegerField(db_column='Local', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor')  # Field name made lowercase.
    evento_pagoid = models.IntegerField(db_column='Evento pagoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Evento'


class Feedback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    inscriçãoid = models.ForeignKey('Inscrição', models.DO_NOTHING, db_column='InscriçãoID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Feedback'


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


class Inscrição(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.SET_NULL, default=None, null=True, db_column='EventoID')  # Field name made lowercase.
    participanteutilizadorid = models.ForeignKey('Participante', models.SET_NULL, default=None, null=True, db_column='ParticipanteUtilizadorID')  # Field name made lowercase.
    utilizador_eventoid = models.IntegerField(db_column='Utilizador_EventoID')  # Field name made lowercase.
    checkin = models.IntegerField(db_column='CheckIn')  # Field name made lowercase.
    valido = models.IntegerField(db_column='Valido')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Inscrição'


class Mensagem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey('Utilizador', models.SET_NULL, default=None, null=True, db_column='UtilizadorID')  # Field name made lowercase.
    remetente = models.CharField(db_column='Remetente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    receptor = models.CharField(db_column='Receptor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conteúdo = models.CharField(db_column='Conteúdo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    assunto = models.CharField(db_column='Assunto', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Mensagem'


class OpçãoDeResposta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    perguntaid = models.ForeignKey('Pergunta', models.SET_NULL, default=None, null=True, db_column='PerguntaID')  # Field name made lowercase.
    opção = models.CharField(db_column='Opção', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Opção de resposta'


class Pagamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    divida = models.FloatField(db_column='Divida')  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    inscriçãoid = models.ForeignKey(Inscrição, models.SET_NULL, default=None, null=True, db_column='InscriçãoID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Pagamento'


class Participante(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Participante'


class PedidoDeRecurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.SET_NULL, default=None, null=True, db_column='EventoID')  # Field name made lowercase.
    tipo_de_recursoid = models.ForeignKey('TipoDeRecurso', models.SET_NULL, default=None, null=True, db_column='Tipo de recursoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.
    dia_inicial = models.DateField(db_column='Dia inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_inicial = models.TimeField(db_column='Hora inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dia_final = models.DateField(db_column='Dia final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_final = models.TimeField(db_column='Hora final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    capacidade = models.IntegerField(db_column='Capacidade', blank=True, null=True)  # Field name made lowercase.
    tipo_de_equipamentoid = models.ForeignKey('TipoDeEquipamento', models.SET_NULL, default=None, null=True, db_column='Tipo de equipamentoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_de_serviçoid = models.ForeignKey('TipoDeServiço', models.SET_NULL, default=None, null=True, db_column='Tipo de serviçoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Pedido de recurso'


class Pergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pergunta = models.CharField(db_column='Pergunta', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obrigatório = models.IntegerField(db_column='Obrigatório')  # Field name made lowercase.
    tipo_de_perguntaid = models.ForeignKey('TipoDePergunta', models.SET_NULL, default=None, null=True, db_column='Tipo de perguntaID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Pergunta'


class Proponente(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Proponente'


class Recurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Recurso'


class Requisição(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventoid = models.OneToOneField(Evento, models.SET_NULL, default=None, null=True, db_column='EventoID')  # Field name made lowercase.
    recursoid = models.OneToOneField(Recurso, models.SET_NULL, default=None, null=True, db_column='RecursoID')  # Field name made lowercase.
    dia_inicial = models.DateField(db_column='Dia inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_inicial = models.TimeField(db_column='Hora inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dia_final = models.DateField(db_column='Dia final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_final = models.TimeField(db_column='Hora final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Requisição'


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


class Sala(models.Model):
    recursoid = models.OneToOneField(Recurso, models.DO_NOTHING, db_column='RecursoID', primary_key=True)  # Field name made lowercase.
    edificioid = models.ForeignKey(Edificio, models.SET_NULL, default=None, null=True, db_column='EdificioID')  # Field name made lowercase.
    lugares = models.IntegerField(db_column='Lugares', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Sala'


class Serviço(models.Model):
    recursoid = models.OneToOneField(Recurso, models.DO_NOTHING, db_column='RecursoID', primary_key=True)  # Field name made lowercase.
    tipo_de_serviçoid = models.ForeignKey('TipoDeServiço', models.SET_NULL, default=None, null=True, db_column='Tipo de serviçoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Serviço'


class TipoDeFormulário(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de Formulário'


class TipoDeEquipamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.IntegerField(db_column='Nome', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de equipamento'


class TipoDeEvento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de evento'


class TipoDePergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de pergunta'


class TipoDeRecurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.IntegerField(db_column='Nome', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de recurso'


class TipoDeServiço(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.IntegerField(db_column='Nome', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de serviço'


class Utilizador(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Utilizador'


class UtilizadorMensagem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey(Utilizador, models.SET_NULL, default=None, null=True, db_column='UtilizadorID')  # Field name made lowercase.
    mensagemid = models.ForeignKey(Mensagem, models.SET_NULL, default=None, null=True, db_column='MensagemID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Utilizador_Mensagem'