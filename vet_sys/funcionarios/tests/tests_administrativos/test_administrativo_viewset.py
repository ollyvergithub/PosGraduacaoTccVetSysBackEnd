import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from vet_sys.clientes.api.views.clientes_viewset import ClientesViewSet
from vet_sys.funcionarios.api.views import AdministrativosViewSet

pytestmark = pytest.mark.django_db


def test_view_set(funcionario_administrativo_ollyver, usuario_permissao_atribuicao_funcionario_administrativo):
    request = APIRequestFactory().get('')
    detalhe = AdministrativosViewSet.as_view({'get': 'retrieve'})
    force_authenticate(request, user=usuario_permissao_atribuicao_funcionario_administrativo)
    response = detalhe(request, uuid=funcionario_administrativo_ollyver.uuid)

    assert response.status_code == status.HTTP_200_OK
