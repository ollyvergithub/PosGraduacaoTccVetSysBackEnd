from django.db import models
from vet_sys.models_abstracts import TemNome, Descritivel, ModeloBase


class Pessoa(TemNome, Descritivel, ModeloBase):
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

    cpf = models.CharField(
        "cpf", max_length=20, blank=True, null=True, default="", unique=True
    )

    sexo = models.CharField(
        'Sexo',
        max_length=50,
        choices=SEXO_CHOICES,
        default=SEXO_FEMININO
    )

    tipo_logradouro = models.CharField('Tipo de Logradouro', max_length=50, blank=True, null=True, default='')
    logradouro = models.CharField('Logradouro', max_length=255, blank=True, null=True, default='')
    bairro = models.CharField('Bairro', max_length=255, blank=True, null=True, default='')
    numero = models.CharField('Numero', max_length=255, blank=True, null=True, default='')
    complemento = models.CharField('Complemento', max_length=255, blank=True, null=True, default='')
    cep = models.CharField('CEP', max_length=20, blank=True, null=True, default='')

    ddd = models.CharField('DDD', max_length=4, blank=True, null=True, default='')
    telefone = models.CharField('Telefone', max_length=20, blank=True, null=True, default='')

    ddd_segundo_telefone = models.CharField('DDD', max_length=4, blank=True, null=True, default='')
    segundo_telefone = models.CharField('Telefone', max_length=20, blank=True, null=True, default='')

    data_de_nascimento = models.DateField('Data de nascimento', blank=True, null=True)

    email = models.EmailField("E-mail", max_length=254, blank=True, null=True, default='')

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome
