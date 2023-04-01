import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from vet_sys.pacientes.api.views.pacientes_viewset import PacientesViewSet

pytestmark = pytest.mark.django_db


def test_view_set(paciente_pitoco, usuario_permissao_atribuicao):
    request = APIRequestFactory().get('')
    detalhe = PacientesViewSet.as_view({'get': 'retrieve'})
    force_authenticate(request, user=usuario_permissao_atribuicao)
    response = detalhe(request, uuid=paciente_pitoco.uuid)

    assert response.status_code == status.HTTP_200_OK
