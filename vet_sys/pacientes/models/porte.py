from django.db import models
from vet_sys.models_abstracts import Descritivel, ModeloBase


class Porte(Descritivel, ModeloBase):

    # Porte choices
    PORTE_GIGANTE = 'GIGANTE'
    PORTE_GRANDE = 'GRANDE'
    PORTE_MEDIO = 'MEDIO'
    PORTE_PEQUENO = 'PEQUENO'
    PORTE_MINI = 'MINI'

    PORTE_NOMES = {
        PORTE_GIGANTE: 'Gigante',
        PORTE_GRANDE: 'Grande',
        PORTE_MEDIO: 'Médio',
        PORTE_PEQUENO: 'Pequeno',
        PORTE_MINI: 'Mini',
    }

    PORTE_CHOICES = (
        (PORTE_GIGANTE, PORTE_NOMES[PORTE_GIGANTE]),
        (PORTE_GRANDE, PORTE_NOMES[PORTE_GRANDE]),
        (PORTE_MEDIO, PORTE_NOMES[PORTE_MEDIO]),
        (PORTE_PEQUENO, PORTE_NOMES[PORTE_PEQUENO]),
        (PORTE_MINI, PORTE_NOMES[PORTE_MINI]),
    )

    porte = models.CharField(
        'Porte',
        max_length=50,
        choices=PORTE_CHOICES,
        default=PORTE_MEDIO
    )

    class Meta:
        verbose_name = "Porte"
        verbose_name_plural = "Portes"

    def __str__(self):
        return self.porte
