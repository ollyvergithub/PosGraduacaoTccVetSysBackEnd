import pytest
from django.contrib import admin
from vet_sys.funcionarios.models.administrativo import Administrativo

pytestmark = pytest.mark.django_db


def test_instance_model(funcionario_administrativo_ollyver):
    model = funcionario_administrativo_ollyver
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.nome
    assert model.descricao
    assert model.cpf
    assert model.rg
    assert model.sexo


def test_str_model(funcionario_administrativo_ollyver):
    assert funcionario_administrativo_ollyver.__str__() == 'Ollyver Ottoboni'


def test_admin():
    # pylint: disable=W0212
    assert admin.site._registry[Administrativo]


