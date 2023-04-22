from django.db import models
from .funcionario import Funcionario


class Administrativo(Funcionario):

    rg = models.CharField(
        "RG", max_length=20, blank=True, null=True, default=""
    )

    class Meta:
        permissions = (
            ('acessar_funcionarios_administrativos', 'Acessar Funcionários Administrativos'),
        )

        verbose_name = "Administrativo"
        verbose_name_plural = "Administrativos"

    def __str__(self):
        return self.nome