from datetime import date

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from ..serializers.paciente_serializer import PacienteSerializer
from ...models import Paciente
from django.template.loader import get_template
from django.template.loader import render_to_string
from weasyprint import HTML


class PacientesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'uuid'
    queryset = Paciente.objects.all().order_by('id', )
    serializer_class = PacienteSerializer

    def get_queryset(self):
        qs = Paciente.objects.all()
        nome = self.request.query_params.get('nome')
        if nome:
            qs = qs.filter(nome__unaccent__icontains=nome)

        cliente_uuid = self.request.query_params.get('cliente_uuid')
        if cliente_uuid:
            qs = qs.filter(tutor__uuid=cliente_uuid)

        especie_uuid = self.request.query_params.get('especie_uuid')
        if especie_uuid:
            qs = qs.filter(especie__uuid=especie_uuid)

        raca_uuid = self.request.query_params.get('raca_uuid')
        if raca_uuid:
            qs = qs.filter(raca__uuid=raca_uuid)

        return qs

    @action(
        detail=False,
        methods=['get'],
        url_path='gerar-relatorio-pdf',
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication]
    )
    def gerar_relatorio_pdf(self, request):

        data_atual = date.today().strftime("%d-%m-%Y")
        usuario_logado = self.request.user

        html_string = render_to_string(
            'pdf/pacientes/pdf.html', {'usuario_logado': usuario_logado, 'data_atual': data_atual}).encode(encoding="UTF-8")

        html_pdf = HTML(string=html_string, base_url=self.request.build_absolute_uri()).write_pdf()

        response = HttpResponse(
            html_pdf,
            content_type='application/pdf;'
        )
        response['Content-Disposition'] = 'filename="relatorio-pacientes.pdf"'

        return response
