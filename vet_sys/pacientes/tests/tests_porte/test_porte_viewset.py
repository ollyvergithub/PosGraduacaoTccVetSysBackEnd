import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from vet_sys.pacientes.api.views.portes_viewset import PortesViewSet

pytestmark = pytest.mark.django_db


def test_view_set(porte_mini, usuario_permissao_atribuicao):
    request = APIRequestFactory().get('')
    detalhe = PortesViewSet.as_view({'get': 'retrieve'})
    force_authenticate(request, user=usuario_permissao_atribuicao)
    response = detalhe(request, uuid=porte_mini.uuid)

    assert response.status_code == status.HTTP_200_OK
