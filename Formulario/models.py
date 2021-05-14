from django.db import models

class Formulário(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    tipo_de_eventoid = models.ForeignKey('Evento.TipoDeEvento', models.SET_NULL, default=None, null=True, db_column='Tipo de eventoID') 
    tipo_de_formulárioid = models.ForeignKey('TipoDeFormulário', models.SET_NULL, default=None, null=True, db_column='Tipo de FormulárioID') 
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True) 
    publico = models.IntegerField(db_column='Publico') 

    class Meta:
        managed = True
        db_table = 'Formulário'

class FormulárioPergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    formulárioid = models.OneToOneField('Formulário', models.SET_NULL, default=None, null=True, db_column='FormulárioID') 
    perguntaid = models.OneToOneField('Pergunta', models.SET_NULL, default=None, null=True, db_column='PerguntaID') 

    class Meta:
        managed = True
        db_table = 'Formulário_Pergunta'


class OpçãoDeResposta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    perguntaid = models.ForeignKey('Pergunta', models.SET_NULL, default=None, null=True, db_column='PerguntaID') 
    opção = models.CharField(db_column='Opção', max_length=255, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Opção de resposta'




class Pergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    pergunta = models.CharField(db_column='Pergunta', max_length=255, blank=True, null=True) 
    obrigatório = models.IntegerField(db_column='Obrigatório') 
    tipo_de_perguntaid = models.ForeignKey('TipoDePergunta', models.SET_NULL, default=None, null=True, db_column='Tipo de perguntaID') 

    class Meta:
        managed = True
        db_table = 'Pergunta'

class Resposta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    perguntaid = models.ForeignKey('Formulario.Pergunta', models.SET_NULL, default=None, null=True, db_column='PerguntaID') 
    eventoid = models.ForeignKey('Evento.Evento', models.SET_NULL, default=None, null=True, db_column='EventoID') 
    inscriçãoid = models.ForeignKey('Inscriçao.Inscrição', models.SET_NULL, default=None, null=True, db_column='InscriçãoID') 
    feedbackid = models.ForeignKey('Inscriçao.Feedback', models.SET_NULL, default=None, null=True, db_column='FeedbackID') 
    resposta = models.CharField(db_column='Resposta', max_length=2048, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Resposta'


class TipoDeFormulário(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Tipo de Formulário'

class TipoDePergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Tipo de pergunta'
