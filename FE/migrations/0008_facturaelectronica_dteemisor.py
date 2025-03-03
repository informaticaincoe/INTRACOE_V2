# Generated by Django 5.1.3 on 2025-02-09 00:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FE', '0007_receptor_fe_rename_emisor_emisor_fe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaelectronica',
            name='dteemisor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='facturas_emisor_FE', to='FE.emisor_fe'),
            preserve_default=False,
        ),
    ]
