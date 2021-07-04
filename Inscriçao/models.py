from django.db import models


class Inscrição(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    eventoid = models.ForeignKey('Evento.Evento', models.DO_NOTHING, db_column='EventoID') 
    participanteutilizadorid = models.ForeignKey('Utilizadores.Participante', models.DO_NOTHING, db_column='ParticipanteUtilizadorID') 
    checkin = models.BooleanField(db_column='CheckIn') 
    valido = models.BooleanField(db_column='Valido') 

    class Meta:
        managed = True
        db_table = 'Inscrição'
    
    def __str__(self):
        return str(self.id)


class Feedback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    inscriçãoid = models.ForeignKey('Inscrição', models.DO_NOTHING, db_column='InscriçãoID')
    
    class Meta:
        managed = True
        db_table = 'Feedback'
    
    def __str__(self):
        return str(self.id)


class Pagamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    divida = models.FloatField(db_column='Divida') 
    data = models.DateField(db_column='Data', blank=True, null=True) 
    hora = models.TimeField(db_column='Hora', blank=True, null=True) 
    inscriçãoid = models.ForeignKey('Inscrição', models.SET_NULL, default=None, null=True, db_column='InscriçãoID') 

    class Meta:
        managed = True
        db_table = 'Pagamento'
    
    def __str__(self):
        return str(self.id)