from datetime import date

from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ...models.consulta import Consulta
from rest_framework.decorators import action
from django.template.loader import render_to_string
from weasyprint import HTML
from ..serializer.consulta_serializer import ConsultaSerializer


class ConsultasViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'uuid'
    queryset = Consulta.objects.all().order_by('-data_da_consulta')
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        qs = Consulta.objects.all().order_by('-data_da_consulta')

        data_da_consulta = self.request.query_params.get('data_da_consulta')
        if data_da_consulta:
            qs = qs.filter(data_da_consulta=data_da_consulta)

        paciente_uuid = self.request.query_params.get('paciente_uuid')
        if paciente_uuid:
            qs = qs.filter(paciente__uuid=paciente_uuid)

        cliente_uuid = self.request.query_params.get('cliente_uuid')
        if cliente_uuid:
            qs = qs.filter(cliente__uuid=cliente_uuid)

        veterinario_uuid = self.request.query_params.get('veterinario_uuid')
        if veterinario_uuid:
            qs = qs.filter(veterinario__uuid=veterinario_uuid)

        return qs

    @action(
        detail=False,
        methods=['post'],
        url_path='gerar-relatorio-pdf',
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication]
    )
    def gerar_relatorio_pdf(self, request):
        from vet_sys.consultas.api.serializer.validation_serializers import GerarRelatorioPdfValidateSerializer

        data_atual = date.today().strftime("%d-%m-%Y")
        usuario_logado = self.request.user

        query = GerarRelatorioPdfValidateSerializer(data=self.request.data)
        query.is_valid(raise_exception=True)

        uuids_consultas = self.request.data.get('uuids_consultas', None)

        consultas = Consulta.objects.filter(uuid__in=uuids_consultas)

        html_string = render_to_string(
            'pdf/consultas/pdf.html',
            {'consultas': consultas, 'usuario_logado': usuario_logado, 'data_atual': data_atual}).encode(
            encoding="UTF-8")

        html_pdf = HTML(string=html_string, base_url=self.request.build_absolute_uri()).write_pdf()

        response = HttpResponse(
            html_pdf,
            content_type='application/pdf;'
        )
        response['Content-Disposition'] = 'filename="relatorio-consultas.pdf"'

        return response