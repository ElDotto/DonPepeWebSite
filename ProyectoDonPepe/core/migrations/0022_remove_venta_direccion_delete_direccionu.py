# Generated by Django 5.0.6 on 2024-06-26 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_direccionu_alter_venta_direccion_delete_direccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='direccion',
        ),
        migrations.DeleteModel(
            name='DireccionU',
        ),
    ]
