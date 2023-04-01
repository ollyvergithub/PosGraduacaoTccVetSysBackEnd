import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from vet_sys.pacientes.api.views.especies_viewset import EspeciesViewSet

pytestmark = pytest.mark.django_db


def test_view_set(especie_canina, usuario_permissao_atribuicao):
    request = APIRequestFactory().get('')
    detalhe = EspeciesViewSet.as_view({'get': 'retrieve'})
    force_authenticate(request, user=usuario_permissao_atribuicao)
    response = detalhe(request, uuid=especie_canina.uuid)

    assert response.status_code == status.HTTP_200_OK
