# Generated by Django 4.0.10 on 2023-04-09 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0010_alter_paciente_cor_alter_paciente_especie_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ['id'], 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
    ]