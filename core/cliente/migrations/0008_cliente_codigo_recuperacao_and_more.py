# Generated by Django 5.0.3 on 2024-04-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_clientepreferencias_campeonato_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='codigo_recuperacao',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='clientepreferencias',
            name='opcoes_apostas',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
