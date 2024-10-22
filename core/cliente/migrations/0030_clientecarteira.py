# Generated by Django 5.0.3 on 2024-10-21 16:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0029_delete_clientecarteira'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteCarteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True, null=True)),
                ('token_cartao', models.CharField(max_length=1000, null=True)),
                ('ultimos_quatro_digitos', models.CharField(max_length=1000, null=True)),
                ('data_expiracao', models.CharField(max_length=1000, null=True)),
                ('nome_titular', models.CharField(max_length=1000, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': '"public"."cliente_carteira"',
            },
        ),
    ]
