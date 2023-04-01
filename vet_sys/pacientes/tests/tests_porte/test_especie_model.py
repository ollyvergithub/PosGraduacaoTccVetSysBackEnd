import pytest
from django.contrib import admin
from vet_sys.pacientes.models.especie import Especie
pytestmark = pytest.mark.django_db


def test_instance_model(especie_canina):
    model = especie_canina
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.nome
    assert model.descricao


def test_str_model(especie_canina):
    assert especie_canina.__str__() == 'Canina'


def test_admin():
    # pylint: disable=W0212
    assert admin.site._registry[Especie]

