# Generated by Django 5.0.3 on 2024-08-01 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0021_aposta_casa_aposta_clientepreferencias_stack_aposta'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfis',
            name='nivel',
            field=models.IntegerField(null=True),
        ),
    ]
