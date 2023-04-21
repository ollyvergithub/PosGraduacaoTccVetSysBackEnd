from datetime import date

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

from ..serializers.cliente_serializer import ClienteSerializer
from ...models import Cliente
from rest_framework.decorators import action
from django.template.loader import render_to_string
from weasyprint import HTML
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.ticker import MaxNLocator


class ClientesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'uuid'
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_queryset(self):
        qs = Cliente.objects.all()

        nome = self.request.query_params.get('nome')
        if nome:
            qs = qs.filter(nome__unaccent__icontains=nome)

        cpf = self.request.query_params.get('cpf')
        if cpf:
            qs = qs.filter(cpf__unaccent__icontains=cpf)


        telefone = self.request.query_params.get('telefone')
        if telefone:
            qs = qs.filter(telefone__unaccent__icontains=telefone)

        paciente_uuid = self.request.query_params.get('paciente_uuid')
        if paciente_uuid:
            qs = qs.filter(paciente__uuid=paciente_uuid)

        return qs

    @action(
        detail=False,
        methods=['post'],
        url_path='gerar-relatorio-pdf',
        permission_classes=[AllowAny],
        authentication_classes=[TokenAuthentication]
    )
    def gerar_relatorio_pdf(self, request):
        from vet_sys.clientes.api.serializers.validation_serializers import GerarRelatorioPdfValidateSerializer

        data_atual = date.today().strftime("%d-%m-%Y")
        usuario_logado = self.request.user

        query = GerarRelatorioPdfValidateSerializer(data=self.request.data)
        query.is_valid(raise_exception=True)

        uuids_clientes = self.request.data.get('uuids_clientes', None)

        clientes = Cliente.objects.filter(uuid__in=uuids_clientes)
        clientes_serializer = ClienteSerializer(clientes, many=True).data

        html_string = render_to_string(
            'pdf/clientes/pdf.html',
            {'clientes': clientes_serializer, 'usuario_logado': usuario_logado, 'data_atual': data_atual}).encode(
            encoding="UTF-8")

        html_pdf = HTML(string=html_string, base_url=self.request.build_absolute_uri()).write_pdf()

        response = HttpResponse(
            html_pdf,
            content_type='application/pdf;'
        )
        response['Content-Disposition'] = 'filename="relatorio-clientes.pdf"'

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
            result = Cliente.objects.filter(criado_em__month=i).count()
            quantidade_de_cadastros_por_mes.append(result)

        fig, ax = plt.subplots()

        # Convertendo valores eixo y (Quantidade para inteiro)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        ax.bar(meses, quantidade_de_cadastros_por_mes)

        ax.set(xlabel='Meses', ylabel='Quantidade', title='Número de clientes cadastrados por mês (2023)')
        ax.grid()

        response = HttpResponse(content_type='image/png')
        canvas = FigureCanvasAgg(fig)
        canvas.print_png(response)
        matplotlib.pyplot.close()
        return response