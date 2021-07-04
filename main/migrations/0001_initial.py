# Generated by Django 3.2.4 on 2021-07-03 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Utilizadores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('remetente', models.CharField(blank=True, db_column='Remetente', max_length=255, null=True)),
                ('receptor', models.CharField(blank=True, db_column='Receptor', max_length=255, null=True)),
                ('conteúdo', models.CharField(blank=True, db_column='Conteúdo', max_length=255, null=True)),
                ('data', models.DateField(blank=True, db_column='Data', null=True)),
                ('assunto', models.CharField(blank=True, db_column='Assunto', max_length=255, null=True)),
                ('utilizadorid', models.ForeignKey(db_column='UtilizadorID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Utilizadores.utilizador')),
            ],
            options={
                'db_table': 'Mensagem',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UtilizadorMensagem',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('mensagemid', models.ForeignKey(db_column='MensagemID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.mensagem')),
                ('utilizadorid', models.ForeignKey(db_column='UtilizadorID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Utilizadores.utilizador')),
            ],
            options={
                'db_table': 'Utilizador_Mensagem',
                'managed': True,
            },
        ),
    ]
