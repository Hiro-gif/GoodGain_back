# Generated by Django 5.0.3 on 2024-04-05 13:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='assinatura',
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_nascimento',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='imagem',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
