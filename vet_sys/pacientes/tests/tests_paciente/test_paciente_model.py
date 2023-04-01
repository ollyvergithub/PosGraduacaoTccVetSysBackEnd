import pytest
from django.contrib import admin
from vet_sys.pacientes.models.paciente import Paciente
from vet_sys.pacientes.models.especie import Especie
from vet_sys.clientes.models.cliente import Cliente

pytestmark = pytest.mark.django_db


def test_instance_model(
        paciente_pitoco,
):
    model = paciente_pitoco
    assert isinstance(model, Paciente)
    assert isinstance(model.especie, Especie)
    assert isinstance(model.tutor, Cliente)
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.nome
    assert model.tutor
    assert model.especie
    assert model.raca
    assert model.porte
    assert model.sexo
    assert model.data_nasc
    assert model.pelagem
    assert model.cor


def test_str_model(paciente_pitoco):
    assert paciente_pitoco.__str__() == 'Pitoco'


def test_admin():
    # pylint: disable=W0212
    assert admin.site._registry[Paciente]
