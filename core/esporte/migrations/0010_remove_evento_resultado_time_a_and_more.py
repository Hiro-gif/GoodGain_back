# Generated by Django 5.0.3 on 2024-05-09 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esporte', '0009_alter_evento_resultado_time_a_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='resultado_time_a',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='resultado_time_b',
        ),
    ]
