# Generated by Django 4.0.10 on 2023-04-23 14:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0012_alter_paciente_tutor'),
        ('funcionarios', '0005_veterinario'),
        ('clientes', '0003_alter_cliente_sexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('data_da_consulta', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Data da consulta')),
                ('tipo_de_consulta', models.CharField(blank=True, choices=[('NOVA', 'Nova'), ('RETORNO', 'Retorno')], default='NOVA', max_length=50, null=True, verbose_name='Tipo de consulta')),
                ('ficha_clinica', models.TextField(blank=True, null=True, verbose_name='Ficha Clínica')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultas_do_cliente', to='clientes.cliente', verbose_name='Cliente')),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultas_do_paciente', to='pacientes.paciente', verbose_name='Paciente')),
                ('veterinario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultas_do_veterinario', to='funcionarios.veterinario', verbose_name='Veterinario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
