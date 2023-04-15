import pytest
pytestmark = pytest.mark.django_db


def test_instance_model(pessoa_ollyver):
    model = pessoa_ollyver
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.nome
    assert model.descricao
    assert model.cpf
    assert model.sexo


def test_str_model(pessoa_ollyver):
    assert pessoa_ollyver.__str__() == 'Ollyver Ottoboni'

