from datetime import date
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from vet_sys.funcionarios.models.administrativo import Administrativo
from vet_sys.funcionarios.api.serializers.administrativo_serializer import AdministrativoSerializer
from rest_framework.decorators import action
from django.template.loader import render_to_string
from weasyprint import HTML


class AdministrativosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'uuid'
    queryset = Administrativo.objects.all()
    serializer_class = AdministrativoSerializer

    def get_queryset(self):
        qs = Administrativo.objects.all()

        nome = self.request.query_params.get('nome')
        if nome:
            qs = qs.filter(nome__unaccent__icontains=nome)

        cpf = self.request.query_params.get('cpf')
        if cpf:
            qs = qs.filter(cpf__unaccent__icontains=cpf)

        rg = self.request.query_params.get('rg')
        if rg:
            qs = qs.filter(rg__unaccent__icontains=rg)

        telefone = self.request.query_params.get('telefone')
        if telefone:
            qs = qs.filter(telefone__unaccent__icontains=telefone)

        return qs

    @action(
        detail=False,
        methods=['post'],
        url_path='gerar-relatorio-pdf',
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication]
    )
    def gerar_relatorio_pdf(self, request):
        from vet_sys.funcionarios.api.serializers.validation_serializers import GerarRelatorioPdfValidateSerializer

        data_atual = date.today().strftime("%d-%m-%Y")
        usuario_logado = self.request.user

        query = GerarRelatorioPdfValidateSerializer(data=self.request.data)
        query.is_valid(raise_exception=True)

        uuids_administrativos = self.request.data.get('uuids_administrativos', None)

        administrativos = Administrativo.objects.filter(uuid__in=uuids_administrativos)

        html_string = render_to_string(
            'pdf/administrativos/pdf.html',
            {'funcionarios': administrativos, 'usuario_logado': usuario_logado, 'data_atual': data_atual}).encode(
            encoding="UTF-8")

        html_pdf = HTML(string=html_string, base_url=self.request.build_absolute_uri()).write_pdf()

        response = HttpResponse(
            html_pdf,
            content_type='application/pdf;'
        )
        response['Content-Disposition'] = 'filename="relatorio-funcionarios.pdf"'

        return response
