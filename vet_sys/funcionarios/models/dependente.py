from django.db import models
from vet_sys.models_abstracts import ModeloBase


class Dependente(ModeloBase):
    SEXO_MASCULINO = 'MASCULINO'
    SEXO_FEMININO = 'FEMININO'

    SEXO_NOMES = {
        SEXO_MASCULINO: 'Masculino',
        SEXO_FEMININO: 'Feminino',
    }

    SEXO_CHOICES = (
        (SEXO_MASCULINO, SEXO_NOMES[SEXO_MASCULINO]),
        (SEXO_FEMININO, SEXO_NOMES[SEXO_FEMININO]),
    )

    nome = models.CharField('Nome', max_length=160)

    data_de_nascimento = models.DateField('Data de nascimento', blank=True, null=True)

    sexo = models.CharField(
        'Sexo',
        max_length=50,
        choices=SEXO_CHOICES,
        default=SEXO_FEMININO,
        blank=True,
        null=True,
    )

    funcionario = models.ForeignKey('funcionarios.Administrativo', on_delete=models.CASCADE,
                                    related_name='dependentes_do_funcionario', verbose_name="Funcionario", null=True,
                                    blank=True)

    class Meta:
        verbose_name = "Dependente"
        verbose_name_plural = "Dependentes"
        ordering = ['id']

    def __str__(self):
        return self.nome
