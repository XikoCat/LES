# Generated by Django 3.2.3 on 2021-05-20 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inscriçao', '0001_initial'),
        ('Evento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulário',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=255, null=True)),
                ('publico', models.IntegerField(db_column='Publico')),
                ('tipo_de_eventoid', models.ForeignKey(db_column='Tipo de eventoID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Evento.tipodeevento')),
            ],
            options={
                'db_table': 'Formulário',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('pergunta', models.CharField(blank=True, db_column='Pergunta', max_length=255, null=True)),
                ('obrigatório', models.BooleanField(db_column='Obrigatório')),
                ('numero_maximo_de_escolhas', models.IntegerField(db_column='NumeroMaximoDeEscolhas', default=None, null=True, verbose_name=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'db_table': 'Pergunta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoDeFormulário',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Tipo de Formulário',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoDePergunta',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Tipo de pergunta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('resposta', models.CharField(blank=True, db_column='Resposta', max_length=2048, null=True)),
                ('eventoid', models.ForeignKey(db_column='EventoID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Evento.evento')),
                ('feedbackid', models.ForeignKey(db_column='FeedbackID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inscriçao.feedback')),
                ('inscriçãoid', models.ForeignKey(db_column='InscriçãoID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inscriçao.inscrição')),
                ('perguntaid', models.ForeignKey(db_column='PerguntaID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formulario.pergunta')),
            ],
            options={
                'db_table': 'Resposta',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='pergunta',
            name='tipo_de_perguntaid',
            field=models.ForeignKey(db_column='Tipo de perguntaID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formulario.tipodepergunta'),
        ),
        migrations.CreateModel(
            name='OpçãoDeResposta',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('opção', models.CharField(blank=True, db_column='Opção', max_length=255, null=True)),
                ('perguntaid', models.ForeignKey(db_column='PerguntaID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formulario.pergunta')),
            ],
            options={
                'db_table': 'Opção de resposta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FormulárioPergunta',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('formulárioid', models.OneToOneField(db_column='FormulárioID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formulario.formulário')),
                ('perguntaid', models.OneToOneField(db_column='PerguntaID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formulario.pergunta')),
            ],
            options={
                'db_table': 'Formulário_Pergunta',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='formulário',
            name='tipo_de_formulárioid',
            field=models.ForeignKey(db_column='Tipo de FormulárioID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formulario.tipodeformulário'),
        ),
    ]
