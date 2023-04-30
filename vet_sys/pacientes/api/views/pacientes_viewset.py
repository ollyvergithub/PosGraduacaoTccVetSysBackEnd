from datetime import date

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.ticker import MaxNLocator
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from ..serializers.paciente_serializer import PacienteSerializer
from ...models import Paciente
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
        methods=['post'],
        url_path='gerar-relatorio-pdf',
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication]
    )
    def gerar_relatorio_pdf(self, request):
        from vet_sys.pacientes.api.serializers.validation_serializers import GerarRelatorioPdfValidateSerializer

        data_atual = date.today().strftime("%d-%m-%Y")
        usuario_logado = self.request.user

        query = GerarRelatorioPdfValidateSerializer(data=self.request.data)
        query.is_valid(raise_exception=True)

        uuids_pacientes = self.request.data.get('uuids_pacientes', None)

        pacientes = Paciente.objects.filter(uuid__in=uuids_pacientes)

        html_string = render_to_string(
            'pdf/pacientes/pdf.html', {'pacientes': pacientes, 'usuario_logado': usuario_logado, 'data_atual': data_atual}).encode(
            encoding="UTF-8")

        html_pdf = HTML(string=html_string, base_url=self.request.build_absolute_uri()).write_pdf()

        response = HttpResponse(
            html_pdf,
            content_type='application/pdf;'
        )
        response['Content-Disposition'] = 'filename="relatorio-pacientes.pdf"'

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
            result = Paciente.objects.filter(criado_em__month=i, criado_em__year=ano).count()
            quantidade_de_cadastros_por_mes.append(result)

        fig, ax = plt.subplots()

        # Convertendo valores eixo y (Quantidade para inteiro)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        ax.bar(meses, quantidade_de_cadastros_por_mes)

        ax.set(xlabel='Meses', ylabel='Quantidade', title=f'Número de pacientes por mês em {ano}')
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

        result = Paciente.objects.filter(criado_em__month=mes, criado_em__year=ano).count()

        fig, ax = plt.subplots()

        # Convertendo valores eixo y (Quantidade para inteiro)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        meses = {"01": "Jan", "02": "Fev", "03": "Mar", "04": "Abr", "05": "Mai", "06": "Jun", "07": "Jul", "08": "Ago",
                 "09": "Set", "10": "Out", "11": "Nov", "12": "Dez"}

        ax.bar(meses[mes], result)

        ax.set(xlabel='Mes', ylabel='Quantidade', title=f"Número de pacientes em {meses[mes]} de {ano}")
        ax.grid()

        response = HttpResponse(content_type='image/png')
        canvas = FigureCanvasAgg(fig)
        canvas.print_png(response)
        matplotlib.pyplot.close()
        return response

    @action(
        detail=False,
        methods=['get'],
        url_path='gerar-estatisticas',
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication]
    )
    def gerar_estatisticas(self, request):

        quantidade_de_cadastros_por_mes = []
        for i in range(1, 13):
            result = Paciente.objects.filter(criado_em__month=i).count()
            quantidade_de_cadastros_por_mes.append(result)

        fig, ax = plt.subplots()

        # Convertendo valores eixo y (Quantidade para inteiro)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        ax.bar(meses, quantidade_de_cadastros_por_mes)

        ax.set(xlabel='Meses', ylabel='Quantidade', title='Número de pacientes cadastrados por mês (2023)')
        ax.grid()

        response = HttpResponse(content_type='image/png')
        canvas = FigureCanvasAgg(fig)
        canvas.print_png(response)
        matplotlib.pyplot.close()
        return response
