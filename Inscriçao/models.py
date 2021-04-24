from django.db import models

class Feedback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    inscriçãoid = models.ForeignKey('Inscrição', models.DO_NOTHING, db_column='InscriçãoID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Feedback'

class Inscrição(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventoid = models.ForeignKey('Evento.Evento', models.SET_NULL, default=None, null=True, db_column='EventoID')  # Field name made lowercase.
    participanteutilizadorid = models.ForeignKey('Utilizadores.Participante', models.SET_NULL, default=None, null=True, db_column='ParticipanteUtilizadorID')  # Field name made lowercase.
    utilizador_eventoid = models.IntegerField(db_column='Utilizador_EventoID')  # Field name made lowercase.
    checkin = models.IntegerField(db_column='CheckIn')  # Field name made lowercase.
    valido = models.IntegerField(db_column='Valido')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Inscrição'


class Pagamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    divida = models.FloatField(db_column='Divida')  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    inscriçãoid = models.ForeignKey('Inscrição', models.SET_NULL, default=None, null=True, db_column='InscriçãoID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Pagamento'
