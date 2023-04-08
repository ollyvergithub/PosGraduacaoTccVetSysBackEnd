from django.db import models
from vet_sys.models_abstracts import TemNome, Descritivel, ModeloBase


class Paciente(TemNome, Descritivel, ModeloBase):
    SEXO_MACHO = 'MACHO'
    SEXO_FEMEA = 'FEMEA'

    SEXO_NOMES = {
        SEXO_MACHO: 'Macho',
        SEXO_FEMEA: 'Fêmea',
    }

    SEXO_CHOICES = (
        (SEXO_MACHO, SEXO_NOMES[SEXO_MACHO]),
        (SEXO_FEMEA, SEXO_NOMES[SEXO_FEMEA]),
    )

    tutor = models.ForeignKey('clientes.Cliente', on_delete=models.PROTECT,
                              related_name='pacientes_do_cliente', verbose_name="Tutor", null=True, blank=True)

    especie = models.ForeignKey('Especie', on_delete=models.PROTECT,
                                related_name='pacientes_da_especie')

    raca = models.ForeignKey('Raca', on_delete=models.PROTECT,
                             related_name='pacientes_da_raca')

    porte = models.ForeignKey('Porte', on_delete=models.PROTECT,
                              related_name='pacientes_do_porte')

    sexo = models.CharField(
        'Sexo',
        max_length=50,
        choices=SEXO_CHOICES,
        default=SEXO_FEMEA
    )

    data_nasc = models.DateField("Data de nascimento aproximada", null=True, blank=True)

    pelagem = models.CharField("Pelagem", max_length=100, blank=True, default="")

    cor = models.CharField("Cor", max_length=100, blank=True, default="")

    peso = models.FloatField("Peso", null=True, blank=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nome
