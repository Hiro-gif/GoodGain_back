# Generated by Django 5.0.3 on 2024-05-22 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esporte', '0013_remove_performacetime_campeonato_season_dat_fim_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performacetime',
            name='season',
        ),
        migrations.RemoveField(
            model_name='performacetime',
            name='time',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
        migrations.DeleteModel(
            name='PerformaceTime',
        ),
    ]
