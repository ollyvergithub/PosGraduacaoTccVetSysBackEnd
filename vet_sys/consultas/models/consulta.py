from datetime import date

from django.db import models
from vet_sys.models_abstracts import ModeloBase


class Consulta(ModeloBase):
    TIPO_CONSULTA_NOVA = 'NOVA'
    TIPO_CONSULTA_RETORNO = 'RETORNO'

    TIPO_CONSULTA_NOMES = {
        TIPO_CONSULTA_NOVA: 'Nova',
        TIPO_CONSULTA_RETORNO: 'Retorno',
    }

    TIPO_CONSULTA_CHOICES = (
        (TIPO_CONSULTA_NOVA, TIPO_CONSULTA_NOMES[TIPO_CONSULTA_NOVA]),
        (TIPO_CONSULTA_RETORNO, TIPO_CONSULTA_NOMES[TIPO_CONSULTA_RETORNO]),
    )

    data_da_consulta = models.DateField("Data da consulta", null=True, blank=True, default=date.today)

    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.SET_NULL,
        related_name='consultas_do_paciente',
        verbose_name="Paciente",
        null=True,
        blank=True
    )

    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.SET_NULL,
        related_name='consultas_do_cliente',
        verbose_name="Cliente",
        null=True,
        blank=True
    )

    veterinario = models.ForeignKey(
        'funcionarios.Veterinario',
        on_delete=models.SET_NULL,
        related_name='consultas_do_veterinario',
        verbose_name="Veterinario",
        null=True,
        blank=True
    )

    tipo_de_consulta = models.CharField(
        'Tipo de consulta',
        max_length=50,
        choices=TIPO_CONSULTA_CHOICES,
        default=TIPO_CONSULTA_NOVA,
        null=True,
        blank=True
    )

    ficha_clinica = models.TextField("Ficha Clínica", blank=True, null=True)

    class Meta:
        permissions = (
            ('acessar_consultas', 'Acessar Consultas'),
        )

        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        ordering = ['-data_da_consulta']

    def __str__(self):
        texto = 'Consulta'
        if self.paciente:
            texto += f" {self.paciente}"

        return texto
