import pytest
from vet_sys.pacientes.api.serializers.paciente_serializer import PacienteSerializer

pytestmark = pytest.mark.django_db


def test_serializer(paciente_pitoco):
    serializer = PacienteSerializer(paciente_pitoco)
    # fields = ('uuid', 'nome', 'especie', 'raca', 'porte', 'sexo', 'tutor', 'data_nasc', 'pelagem', 'cor')
    assert serializer.data is not None
    assert serializer.data['uuid']
    assert serializer.data['nome']
    assert serializer.data['descricao']
    assert serializer.data['especie']
    assert serializer.data['tutor']
    assert serializer.data['raca']
    assert serializer.data['porte']
    assert serializer.data['sexo']
    assert serializer.data['data_nasc']
    assert serializer.data['pelagem']
    assert serializer.data['cor']
