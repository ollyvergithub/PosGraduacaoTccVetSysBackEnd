import pytest
from django.contrib import admin
from vet_sys.pacientes.models.raca import Raca
pytestmark = pytest.mark.django_db


def test_instance_model(raca_schnauzer):
    model = raca_schnauzer
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.nome
    assert model.descricao


def test_str_model(raca_schnauzer):
    assert raca_schnauzer.__str__() == 'Schnauzer'


def test_admin():
    # pylint: disable=W0212
    assert admin.site._registry[Raca]

