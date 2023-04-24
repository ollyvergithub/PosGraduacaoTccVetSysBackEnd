import pytest
from vet_sys.consultas.api.serializer.consulta_serializer import ConsultaSerializer

pytestmark = pytest.mark.django_db


def test_serializer(consulta_01):
    serializer = ConsultaSerializer(consulta_01)
    assert serializer.data is not None
    assert serializer.data['id']
    assert serializer.data['uuid']
    assert serializer.data['data_da_consulta']
    assert serializer.data['paciente']
    assert serializer.data['cliente']
    assert serializer.data['veterinario']
    assert serializer.data['tipo_de_consulta']
    assert serializer.data['ficha_clinica']

