# Generated by Django 3.2.4 on 2021-06-22 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recurso', '0002_alter_tipoderecurso_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='edificioid',
            field=models.ForeignKey(db_column='EdificioID', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Recurso.edificio', verbose_name='Edificio'),
        ),
    ]
