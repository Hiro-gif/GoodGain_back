# Generated by Django 5.0.3 on 2024-04-24 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_clientepreferencias_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClientePreferencias',
        ),
    ]