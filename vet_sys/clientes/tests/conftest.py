from datetime import date

import pytest
from model_bakery import baker

pytestmark = pytest.mark.django_db


@pytest.fixture
def usuario_permissao_atribuicao_clientes():
    from django.contrib.auth import get_user_model
    senha = 'Sgp0418'
    login = '7210418'
    email = 'sme@amcom.com.br'
    User = get_user_model()
    user = User.objects.create_user(username=login, password=senha, email=email)
    user.save()
    return user


@pytest.fixture
def especie_canina_clientes():
    return baker.make(
        'Especie',
        nome='Canina',
        descricao='Descrição espécie Canina',
    )


@pytest.fixture
def porte_mini_clientes():
    return baker.make(
        'Porte',
        porte='Mini',
        descricao='Esta é a descrição do Porte Mini',
    )


@pytest.fixture
def raca_schnauzer_clientes():
    return baker.make(
        'Raca',
        nome='Schnauzer',
        descricao='Descrição Raça Schnauzer',
    )


@pytest.fixture
def paciente_pitoco_clientes(
        especie_canina_clientes,
        raca_schnauzer_clientes,
        porte_mini_clientes,
        cliente_ollyver_clientes

):
    return baker.make(
        'Paciente',
        nome='Pitoco',
        tutor=cliente_ollyver_clientes,
        especie=especie_canina_clientes,
        raca=raca_schnauzer_clientes,
        porte=porte_mini_clientes,
        sexo='Macho',
        data_nasc=date(2021, 6, 16),
        pelagem="Curta",
        cor="Cinza",
        descricao="Lindo e carinhoso",
    )


@pytest.fixture
def paciente_lorita_clientes(
        especie_canina_clientes,
        raca_schnauzer_clientes,
        porte_mini_clientes,
        cliente_ollyver_clientes,
):
    return baker.make(
        'Paciente',
        tutor=cliente_ollyver_clientes,
        especie=especie_canina_clientes,
        raca=raca_schnauzer_clientes,
        porte=porte_mini_clientes,
        sexo='Macho',
        data_nasc=date(2021, 6, 16),
        pelagem="Curta",
        cor="Cinza",
    )


@pytest.fixture
def cliente_ollyver_clientes():
    return baker.make(
        'Cliente',
        nome='Ollyver Ottoboni',
        cpf='824.001.090-36',
        sexo='Masculino',
    )


@pytest.fixture
def cliente_susi_clientes(
        paciente_pitoco_clientes,
):
    return baker.make(
        'Cliente',
        nome='Susi Nishimura',
        cpf='433.568.660-95',
        sexo='Feminino',
        paciente=[paciente_pitoco_clientes],
        descricao='Esta é a descrição do cliente Susi Nishimura',
    )
