# Generated by Django 3.2.4 on 2021-07-04 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Evento', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='formuláriofeedbackid',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='formulárioinscriçãoid',
        ),
    ]