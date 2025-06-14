# Generated by Django 5.2 on 2025-04-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OMCS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='pending_doctors',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]
