# Generated by Django 5.2 on 2025-05-29 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OMCS', '0005_alter_appointments_hospitalid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='hospitalid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OMCS.hospital'),
        ),
    ]
