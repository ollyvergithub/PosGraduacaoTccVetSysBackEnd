import pytest
from model_bakery import baker
pytestmark = pytest.mark.django_db


@pytest.fixture
def usuario_permissao_atribuicao():

    from django.contrib.auth import get_user_model
    senha = 'Sgp0418'
    login = '7210418'
    email = 'sme@amcom.com.br'
    User = get_user_model()
    user = User.objects.create_user(username=login, password=senha, email=email)
    user.save()
    return user


@pytest.fixture
def especie_canina():
    return baker.make(
        'Especie',
        nome='Canina',
        descricao='Descrição espécie Canina',
    )


@pytest.fixture
def porte_mini():
    return baker.make(
        'Porte',
        porte='Mini',
        descricao='Esta é a descrição do Porte Mini',
    )


@pytest.fixture
def raca_schnauzer():
    return baker.make(
        'Raca',
        nome='Schnauzer',
        descricao='Descrição Raça Schnauzer',
    )
