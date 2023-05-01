from datetime import date

import pytest
from model_bakery import baker

pytestmark = pytest.mark.django_db


@pytest.fixture
def usuario_permissao_atribuicao_funcionario_administrativo():
    from django.contrib.auth import get_user_model
    senha = 'Sgp0418'
    login = '7210418'
    email = 'sme@amcom.com.br'
    User = get_user_model()
    user = User.objects.create_user(username=login, password=senha, email=email)
    user.save()
    return user


@pytest.fixture
def funcionario_ollyver():
    return baker.make(
        'Funcionario',
        nome='Ollyver Ottoboni',
        cpf='433.568.660-95',
        sexo='Masculino',
        descricao='Esta é a descrição do funcionário Ollyver Ottoboni',
    )


@pytest.fixture
def funcionario_administrativo_ollyver():
    return baker.make(
        'Administrativo',
        nome='Ollyver Ottoboni',
        cpf='433.568.660-95',
        rg='8.961.424-0',
        sexo='Masculino',
        descricao='Esta é a descrição do funcionário administrativo Ollyver Ottoboni',
    )


@pytest.fixture
def funcionario_veterinario_susi():
    return baker.make(
        'Veterinario',
        nome='Susi Hiromi Nishimura',
        cpf='433.568.660-95',
        crmv='6987-SP',
        sexo='Masculino',
        descricao='Esta é a descrição do funcionário veterinário Susi Hiromi Nishimura',
    )


@pytest.fixture
def dependente_01(
        funcionario_administrativo_ollyver
):
    return baker.make(
        'Dependente',
        nome='Dependente funcionario administrativo Ollyver',
        data_de_nascimento=date(2023, 4, 30),
        sexo="MASCULINO",
        funcionario=funcionario_administrativo_ollyver
    )
