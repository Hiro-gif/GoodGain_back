# Generated by Django 5.0.3 on 2024-04-24 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esporte', '0002_campeonato_status_esporte_status_evento_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='resultado_partida',
            field=models.CharField(null=True),
        ),
    ]