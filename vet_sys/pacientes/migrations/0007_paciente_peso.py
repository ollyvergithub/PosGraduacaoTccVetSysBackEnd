# Generated by Django 4.0.10 on 2023-04-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_paciente_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='peso',
            field=models.FloatField(blank=True, null=True, verbose_name='Peso'),
        ),
    ]
