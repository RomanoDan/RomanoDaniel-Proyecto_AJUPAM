# Generated by Django 5.1.5 on 2025-02-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0004_alter_jugador_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='documento',
            field=models.DecimalField(decimal_places=0, max_digits=8, unique=True),
        ),
    ]
