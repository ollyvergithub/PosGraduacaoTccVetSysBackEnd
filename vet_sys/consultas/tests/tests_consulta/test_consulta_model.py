import pytest
from django.contrib import admin

from vet_sys.consultas.models import Consulta
from vet_sys.funcionarios.models import Veterinario
from vet_sys.pacientes.models.paciente import Paciente
from vet_sys.clientes.models.cliente import Cliente

pytestmark = pytest.mark.django_db


def test_instance_model(
        consulta_01,
        paciente_pitoco_consultas,
        funcionario_veterinario_susi_consultas,
):
    model = consulta_01
    assert isinstance(model, Consulta)
    assert isinstance(model.paciente, Paciente)
    assert isinstance(model.cliente, Cliente)
    assert isinstance(model.veterinario, Veterinario)
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.data_da_consulta
    assert model.paciente
    assert model.cliente
    assert model.veterinario
    assert model.tipo_de_consulta
    assert model.ficha_clinica


def test_str_model(consulta_01):
    assert consulta_01.__str__() == 'Consulta Pitoco'


def test_admin():
    # pylint: disable=W0212
    assert admin.site._registry[Consulta]
