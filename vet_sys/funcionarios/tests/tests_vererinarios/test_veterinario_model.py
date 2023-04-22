import pytest
from django.contrib import admin
from vet_sys.funcionarios.models.veterinario import Veterinario

pytestmark = pytest.mark.django_db


def test_instance_model(funcionario_veterinario_susi):
    model = funcionario_veterinario_susi
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.nome
    assert model.descricao
    assert model.cpf
    assert model.crmv
    assert model.sexo


def test_str_model(funcionario_veterinario_susi):
    assert funcionario_veterinario_susi.__str__() == 'Susi Hiromi Nishimura'


def test_admin():
    # pylint: disable=W0212
    assert admin.site._registry[Veterinario]


