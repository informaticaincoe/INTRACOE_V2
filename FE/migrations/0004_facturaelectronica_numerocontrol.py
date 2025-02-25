# Generated by Django 5.1.3 on 2025-02-08 05:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FE', '0003_rename_fecha_cducidad_token_data_fecha_caducidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaElectronica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_control', models.CharField(blank=True, max_length=31, unique=True)),
                ('codigo_generacion', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('hora_emision', models.TimeField(auto_now_add=True)),
                ('firmado', models.BooleanField(default=False)),
                ('json_original', models.JSONField()),
                ('json_firmado', models.JSONField(blank=True, null=True)),
                ('sello_recepcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NumeroControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(unique=True)),
                ('secuencia', models.IntegerField(default=1)),
            ],
        ),
    ]
