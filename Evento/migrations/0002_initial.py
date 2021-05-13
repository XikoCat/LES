# Generated by Django 3.2 on 2021-05-06 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Evento', '0001_initial'),
        ('Formulario', '0001_initial'),
        ('main', '0002_auto_20210506_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='formuláriofeedbackid',
            field=models.ForeignKey(db_column='FormulárioFeedbackID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feedback', to='Formulario.formulário'),
        ),
        migrations.AddField(
            model_name='evento',
            name='formulárioinscriçãoid',
            field=models.ForeignKey(db_column='FormulárioInscriçãoID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formulario.formulário'),
        ),
        migrations.AddField(
            model_name='evento',
            name='proponenteutilizadorid',
            field=models.ForeignKey(db_column='ProponenteUtilizadorID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.proponente'),
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo_de_eventoid',
            field=models.ForeignKey(db_column='Tipo de eventoID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Evento.tipodeevento'),
        ),
        migrations.AddField(
            model_name='certificadodeparticipação',
            name='eventoid',
            field=models.ForeignKey(db_column='EventoID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Evento.evento'),
        ),
    ]