from django.db import models
from .funcionario import Funcionario


class Veterinario(Funcionario):
    crmv = models.CharField(
        "CRMV", max_length=20, blank=True, null=True, default=""
    )

    class Meta:
        permissions = (
            ('acessar_veterinarios', 'Acessar Veterinários'),
        )

        verbose_name = "Veterinário"
        verbose_name_plural = "Veterinários"

    def __str__(self):
        return self.nome
