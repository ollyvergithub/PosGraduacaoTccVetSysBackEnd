# Generated by Django 4.0.10 on 2023-04-30 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0006_dependente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dependente',
            options={'ordering': ['id'], 'verbose_name': 'Dependente', 'verbose_name_plural': 'Dependentes'},
        ),
    ]
