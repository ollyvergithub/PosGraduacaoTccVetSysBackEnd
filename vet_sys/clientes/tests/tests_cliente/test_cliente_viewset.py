import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from vet_sys.clientes.api.views.clientes_viewset import ClientesViewSet

pytestmark = pytest.mark.django_db


def test_view_set(cliente_susi_clientes, usuario_permissao_atribuicao_clientes):
    request = APIRequestFactory().get('')
    detalhe = ClientesViewSet.as_view({'get': 'retrieve'})
    force_authenticate(request, user=usuario_permissao_atribuicao_clientes)
    response = detalhe(request, uuid=cliente_susi_clientes.uuid)

    assert response.status_code == status.HTTP_200_OK
