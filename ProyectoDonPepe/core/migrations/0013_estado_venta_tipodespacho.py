# Generated by Django 5.0.6 on 2024-06-26 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_tipodespacho_remove_venta_fentrega_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreEs', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='tipodespacho',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.tipodespacho'),
        ),
    ]
