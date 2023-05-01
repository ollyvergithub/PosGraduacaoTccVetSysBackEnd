import pytest
from django.contrib import admin

from vet_sys.funcionarios.models import Dependente
from vet_sys.funcionarios.models.administrativo import Administrativo

pytestmark = pytest.mark.django_db


def test_instance_model(dependente_01):
    model = dependente_01
    assert isinstance(model, Dependente)
    assert isinstance(model.funcionario, Administrativo)
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.nome
    assert model.sexo
    assert model.data_de_nascimento


def test_str_model(dependente_01):
    assert dependente_01.__str__() == 'Dependente funcionario administrativo Ollyver'


def test_admin():
    # pylint: disable=W0212
    assert admin.site._registry[Dependente]


