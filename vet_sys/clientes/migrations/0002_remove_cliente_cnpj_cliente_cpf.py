# Generated by Django 4.0.10 on 2023-03-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cnpj',
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(blank=True, default='', max_length=20, null=True, unique=True, verbose_name='cpf'),
        ),
    ]
