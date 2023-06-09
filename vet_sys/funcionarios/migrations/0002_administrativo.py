# Generated by Django 4.0.10 on 2023-04-22 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrativo',
            fields=[
                ('funcionario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='funcionarios.funcionario')),
                ('rg', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='RG')),
            ],
            options={
                'verbose_name': 'Administrativo',
                'verbose_name_plural': 'Administrativos',
            },
            bases=('funcionarios.funcionario',),
        ),
    ]
