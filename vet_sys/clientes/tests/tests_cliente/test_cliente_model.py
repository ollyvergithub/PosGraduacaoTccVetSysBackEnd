import pytest
from django.contrib import admin
from vet_sys.clientes.models.cliente import Cliente
pytestmark = pytest.mark.django_db


def test_instance_model(cliente_susi_clientes):
    model = cliente_susi_clientes
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.nome
    assert model.descricao
    assert model.cpf
    assert model.sexo
    assert model.paciente


def test_str_model(cliente_susi_clientes):
    assert cliente_susi_clientes.__str__() == 'Susi Nishimura'


def test_admin():
    # pylint: disable=W0212
    assert admin.site._registry[Cliente]

