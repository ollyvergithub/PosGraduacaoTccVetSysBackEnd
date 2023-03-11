import uuid as uuid

from django.db import models


class Descritivel(models.Model):
    descricao = models.TextField('Descrição', blank=True, null=True)

    class Meta:
        abstract = True


class TemNome(models.Model):
    nome = models.CharField('Nome', max_length=160)

    class Meta:
        abstract = True


class TemCriadoEm(models.Model):
    criado_em = models.DateTimeField("Criado em", editable=False, auto_now_add=True)

    class Meta:
        abstract = True


class TemAlteradoEm(models.Model):
    alterado_em = models.DateTimeField("Alterado em", editable=False, auto_now=True)

    class Meta:
        abstract = True


class ModeloBase(TemCriadoEm, TemAlteradoEm):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Expoe explicitamente o model manager para evitar falsos alertas de Unresolved attribute reference for class Model
    objects = models.Manager()

    @classmethod
    def by_id(cls, id):
        return cls.objects.get(id=id)

    class Meta:
        abstract = True


