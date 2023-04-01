import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from vet_sys.pacientes.api.views.racas_viewset import RacasViewSet

pytestmark = pytest.mark.django_db


def test_view_set(raca_schnauzer, usuario_permissao_atribuicao):
    request = APIRequestFactory().get('')
    detalhe = RacasViewSet.as_view({'get': 'retrieve'})
    force_authenticate(request, user=usuario_permissao_atribuicao)
    response = detalhe(request, uuid=raca_schnauzer.uuid)

    assert response.status_code == status.HTTP_200_OK
