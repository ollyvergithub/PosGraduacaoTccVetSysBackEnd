import pytest
from django.contrib import admin
from vet_sys.pacientes.models.porte import Porte
pytestmark = pytest.mark.django_db


def test_instance_model(porte_mini):
    model = porte_mini
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.porte
    assert model.descricao


def test_str_model(porte_mini):
    assert porte_mini.__str__() == 'Mini'


def test_admin():
    # pylint: disable=W0212
    assert admin.site._registry[Porte]

