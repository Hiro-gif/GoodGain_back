# Generated by Django 5.0.3 on 2024-04-17 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_cliente_perfil_clientepreferencias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='clientepreferencias',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='perfis',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]