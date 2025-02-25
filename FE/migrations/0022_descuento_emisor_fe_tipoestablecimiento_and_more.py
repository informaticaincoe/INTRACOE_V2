# Generated by Django 5.1.3 on 2025-02-13 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FE', '0021_alter_receptor_fe_tipo_documento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estdo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='emisor_fe',
            name='tipoestablecimiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FE.tiposestablecimientos'),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='ambiente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FE.ambiente'),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='descuento',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='exentas',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='gravadas',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='iva_percibido',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='iva_retenido',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='no_sujetas',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='retencion_renta',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='sum_total_operaciones',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='suma_exentas',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='suma_gravadas',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='suma_no_sujetas',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='sumas',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='tipomodelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FE.modelofacturacion'),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='tipooperacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FE.condicionoperacion'),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='total_gravadas',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='total_letras',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='total_operaciones',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='total_pagar',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='version',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('preunitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.IntegerField()),
                ('tiene_descuento', models.BooleanField(default=False)),
                ('descuento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FE.descuento')),
            ],
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='producto',
            field=models.ManyToManyField(null=True, to='FE.producto'),
        ),
    ]
