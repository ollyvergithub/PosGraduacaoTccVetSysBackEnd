from datetime import date

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from vet_sys.pacientes.models import Paciente
from ...models.consulta import Consulta
from rest_framework.decorators import action
from django.template.loader import render_to_string
from weasyprint import HTML
from ..serializer.consulta_serializer import ConsultaSerializer, ConsultaHistoricoDeConsultasSerializer
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.ticker import MaxNLocator


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

    @action(
        detail=False,
        methods=['get'],
        url_path='historico-de-consultas-por-paciente',
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication]
    )
    def historico_de_consultas_por_paciente(self, request):
        from vet_sys.consultas.api.serializer.validation_serializers.consulta_validate_serializer import \
            ConsultaPacienteValidateSerializer

        query = ConsultaPacienteValidateSerializer(data=self.request.query_params)
        query.is_valid(raise_exception=True)

        paciente_uuid = request.query_params.get('paciente')
        consulta_uuid = request.query_params.get('consulta')

        paciente = Paciente.objects.get(uuid=paciente_uuid)

        if consulta_uuid:
            consultas = Consulta.objects.filter(paciente=paciente).order_by('-data_da_consulta').exclude(
                uuid=consulta_uuid)
        else:
            consultas = Consulta.objects.filter(paciente=paciente).order_by('-data_da_consulta')

        return Response(ConsultaHistoricoDeConsultasSerializer(consultas, many=True).data)

    @action(
        detail=False,
        methods=['get'],
        url_path='gerar-estatisticas-por-paciente-ano',
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication]
    )
    def gerar_estatisticas_por_paciente_ano(self, request):
        ano = request.query_params.get('ano')
        paciente_uuid = request.query_params.get('paciente')

        paciente = Paciente.objects.get(uuid=paciente_uuid)

        quantidade_de_cadastros_por_mes = []
        for i in range(1, 13):
            result = Consulta.objects.filter(criado_em__month=i, criado_em__year=ano, paciente=paciente).count()
            quantidade_de_cadastros_por_mes.append(result)

        fig, ax = plt.subplots()

        # Convertendo valores eixo y (Quantidade para inteiro)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        ax.bar(meses, quantidade_de_cadastros_por_mes)

        ax.set(xlabel='Meses', ylabel='Quantidade', title=f'Número de consultas por mês de {paciente.nome} em {ano}')
        ax.grid()

        response = HttpResponse(content_type='image/png')
        canvas = FigureCanvasAgg(fig)
        canvas.print_png(response)
        matplotlib.pyplot.close()
        return response

    @action(
        detail=False,
        methods=['get'],
        url_path='gerar-estatisticas-por-ano',
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication]
    )
    def gerar_estatisticas_por_ano(self, request):
        ano = request.query_params.get('ano')

        quantidade_de_cadastros_por_mes = []
        for i in range(1, 13):
            result = Consulta.objects.filter(criado_em__month=i, criado_em__year=ano).count()
            quantidade_de_cadastros_por_mes.append(result)

        fig, ax = plt.subplots()

        # Convertendo valores eixo y (Quantidade para inteiro)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        ax.bar(meses, quantidade_de_cadastros_por_mes)

        ax.set(xlabel='Meses', ylabel='Quantidade', title=f'Número de consultas por mês em {ano}')
        ax.grid()

        response = HttpResponse(content_type='image/png')
        canvas = FigureCanvasAgg(fig)
        canvas.print_png(response)
        matplotlib.pyplot.close()
        return response

    @action(
        detail=False,
        methods=['get'],
        url_path='gerar-estatisticas-por-mes-e-ano',
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication]
    )
    def gerar_estatisticas_por_mes_e_ano(self, request):

        ano = request.query_params.get('ano')
        mes = request.query_params.get('mes')

        result = Consulta.objects.filter(criado_em__month=mes, criado_em__year=ano).count()

        fig, ax = plt.subplots()

        # Convertendo valores eixo y (Quantidade para inteiro)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        meses = {"01": "Jan", "02": "Fev", "03": "Mar", "04": "Abr", "05": "Mai", "06": "Jun", "07": "Jul", "08": "Ago",
                 "09": "Set", "10": "Out", "11": "Nov", "12": "Dez"}

        ax.bar(meses[mes], result)

        ax.set(xlabel='Mes', ylabel='Quantidade', title=f"Número de consultas em {meses[mes]} de {ano}")
        ax.grid()

        response = HttpResponse(content_type='image/png')
        canvas = FigureCanvasAgg(fig)
        canvas.print_png(response)
        matplotlib.pyplot.close()
        return response
