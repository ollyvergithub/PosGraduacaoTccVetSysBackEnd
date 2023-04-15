from datetime import date

import pytest
from model_bakery import baker

pytestmark = pytest.mark.django_db


@pytest.fixture
def pessoa_ollyver():
    return baker.make(
        'Pessoa',
        nome='Ollyver Ottoboni',
        cpf='824.001.090-36',
        sexo='Masculino',
        descricao='Descrição pessoa Ollyver',
    )
