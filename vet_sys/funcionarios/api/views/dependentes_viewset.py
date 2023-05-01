from rest_framework import viewsets


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from vet_sys.funcionarios.api.serializers import DependenteSerializer
from vet_sys.funcionarios.models import Dependente

from rest_framework import filters


class DependentesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'uuid'
    queryset = Dependente.objects.all()
    serializer_class = DependenteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('funcionario__uuid',)

    def get_queryset(self):
        qs = Dependente.objects.all()

        nome = self.request.query_params.get('nome')
        if nome:
            qs = qs.filter(nome__unaccent__icontains=nome)

        return qs

