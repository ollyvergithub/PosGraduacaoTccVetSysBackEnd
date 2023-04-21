import datetime
from django import template

register = template.Library()


@register.filter(name='formata_data')
def formata_data(data):
    data_formatada = " - "
    if data:
        d = datetime.datetime.strptime(str(data), '%Y-%m-%d')
        data_formatada = d.strftime("%d/%m/%Y")

    return f'{data_formatada}'


@register.filter(name='formata_data_e_hora')
def formata_data_e_hora(data):
    data_formatada = " - "
    if data:
        data = data[:10]
        d = datetime.datetime.strptime(str(data), '%Y-%m-%d')
        data_formatada = d.strftime("%d/%m/%Y")

    return f'{data_formatada}'
