# Generated by Django 3.2.3 on 2021-05-30 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Evento', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoderecurso',
            name='tipo_de_equipamentoid',
        ),
        migrations.RemoveField(
            model_name='pedidoderecurso',
            name='tipo_de_serviçoid',
        ),
    ]
