from datetime import date

import pytest
from model_bakery import baker

pytestmark = pytest.mark.django_db


@pytest.fixture
def usuario_permissao_atribuicao_consultas():
    from django.contrib.auth import get_user_model
    senha = 'Sgp0418'
    login = '7210418'
    email = 'sme@amcom.com.br'
    User = get_user_model()
    user = User.objects.create_user(username=login, password=senha, email=email)
    user.save()
    return user


@pytest.fixture
def especie_canina_consultas():
    return baker.make(
        'Especie',
        nome='Canina',
        descricao='Descrição espécie Canina',
    )


@pytest.fixture
def porte_mini_consultas():
    return baker.make(
        'Porte',
        porte='Mini',
        descricao='Esta é a descrição do Porte Mini',
    )


@pytest.fixture
def raca_schnauzer_consultas():
    return baker.make(
        'Raca',
        nome='Schnauzer',
        descricao='Descrição Raça Schnauzer',
    )


@pytest.fixture
def paciente_pitoco_consultas(
        especie_canina_consultas,
        raca_schnauzer_consultas,
        porte_mini_consultas,

):
    return baker.make(
        'Paciente',
        nome='Pitoco',
        especie=especie_canina_consultas,
        raca=raca_schnauzer_consultas,
        porte=porte_mini_consultas,
        sexo='Macho',
        data_nasc=date(2021, 6, 16),
        pelagem="Curta",
        cor="Cinza",
        descricao="Lindo e carinhoso",
    )


@pytest.fixture
def cliente_ollyver_consultas():
    return baker.make(
        'Cliente',
        nome='Ollyver Ottoboni',
        cpf='824.001.090-36',
        sexo='Masculino',
    )


@pytest.fixture
def funcionario_veterinario_susi_consultas():
    return baker.make(
        'Veterinario',
        nome='Susi Hiromi Nishimura',
        cpf='433.568.660-95',
        crmv='6987-SP',
        sexo='Masculino',
        descricao='Esta é a descrição do funcionário veterinário Susi Hiromi Nishimura',
    )


@pytest.fixture
def consulta_01(
        paciente_pitoco_consultas,
        cliente_ollyver_consultas,
        funcionario_veterinario_susi_consultas,
):
    return baker.make(
        'Consulta',
        data_da_consulta=date(2023, 4, 23),
        paciente=paciente_pitoco_consultas,
        cliente=cliente_ollyver_consultas,
        veterinario=funcionario_veterinario_susi_consultas,
        tipo_de_consulta="NOVA",
        ficha_clinica="Nessa data a cachorra foi vacinada com V10",
    )
