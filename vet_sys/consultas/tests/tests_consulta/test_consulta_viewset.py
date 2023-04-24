import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from vet_sys.consultas.api.views.consultas_viewset import ConsultasViewSet

pytestmark = pytest.mark.django_db


def test_view_set(consulta_01, usuario_permissao_atribuicao_consultas):
    request = APIRequestFactory().get('')
    detalhe = ConsultasViewSet.as_view({'get': 'retrieve'})
    force_authenticate(request, user=usuario_permissao_atribuicao_consultas)
    response = detalhe(request, uuid=consulta_01.uuid)

    assert response.status_code == status.HTTP_200_OK
