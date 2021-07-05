from django.db import models

class Formulário(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    tipo_de_eventoid = models.ForeignKey('Evento.TipoDeEvento', models.SET_NULL, default=None, null=True, blank=True, db_column='Tipo de eventoID')
    tipo_de_formulárioid = models.ForeignKey('TipoDeFormulário', models.SET_NULL, default=None, null=True, db_column='Tipo de FormulárioID')
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)
    publico = models.BooleanField(db_column='Publico')
    evento_id = models.ForeignKey('Evento.Evento', models.SET_NULL, default=None, null=True, blank=True, db_column='Evento')

    class Meta:
        managed = True
        db_table = 'Formulário'


class FormulárioPergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    formulárioid = models.ForeignKey('Formulário' , on_delete=models.CASCADE, db_column='FormulárioID')
    perguntaid = models.ForeignKey('Pergunta', on_delete=models.CASCADE, db_column='PerguntaID')
    pos = models.IntegerField(models.SET_NULL, default=0, null=True, db_column='Pos')

    class Meta:
        managed = True
        db_table = 'Formulário_Pergunta'


class OpçãoDeResposta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    perguntaid = models.ForeignKey('Pergunta', models.CASCADE, default=None, null=True, db_column='PerguntaID')
    opção = models.CharField(db_column='Opção', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Opção de resposta'

    def __str__(self):
        return str(self.opção)

class Pergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    pergunta = models.CharField(db_column='Pergunta', max_length=255, blank=True, null=True)
    obrigatório = models.BooleanField(db_column='Obrigatório')
    tipo_de_perguntaid = models.ForeignKey('TipoDePergunta', models.SET_NULL, default=None, null=True, db_column='Tipo de perguntaID')
    numero_maximo_de_escolhas = models.IntegerField(db_column='NumeroMaximoDeEscolhas', default =None, null=True)
    temporario = models.BooleanField(default=False, db_column='temporario')

    class Meta:
        managed = True
        db_table = 'Pergunta'

    def __str__(self):
        return str(self.pergunta)


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

    def __str__(self):
        return str(self.nome)


class TipoDePergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tipo de pergunta'
        
    def __str__(self):
        return str(self.nome)