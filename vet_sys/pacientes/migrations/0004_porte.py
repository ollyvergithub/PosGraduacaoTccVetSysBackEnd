# Generated by Django 4.0.10 on 2023-03-04 16:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_raca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Porte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('porte', models.CharField(choices=[('GIGANTE', 'Gigante'), ('GRANDE', 'Grande'), ('MEDIO', 'Médio'), ('PEQUENO', 'Pequeno'), ('MINI', 'Mini')], default='MEDIO', max_length=50, verbose_name='Porte')),
            ],
            options={
                'verbose_name': 'Porte',
                'verbose_name_plural': 'Portes',
            },
        ),
    ]
