# Generated by Django 5.0.3 on 2024-04-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esporte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campeonato',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='esporte',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='resultado_time_a',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='resultado_time_b',
            field=models.CharField(null=True),
        ),
    ]