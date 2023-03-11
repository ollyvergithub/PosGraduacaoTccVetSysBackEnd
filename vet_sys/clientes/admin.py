from django.contrib import admin

from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'nome', 'cpf', 'ddd', 'telefone')
    search_fields = ('nome', 'cpf')
    list_filter = ('nome', 'cpf')
    readonly_fields = ('uuid', 'id')

    fieldsets = (
        ('', {
            'fields':
                (
                    'nome',
                    'cpf',
                    'sexo',
                    'paciente',
                    'tipo_logradouro',
                    'logradouro',
                    'numero',
                    'bairro',
                    'complemento',
                    'cep',
                    'ddd',
                    'telefone',
                    'ddd_segundo_telefone',
                    'segundo_telefone',
                    'data_de_nascimento',
                    'email',
                    'descricao',
                    'uuid',
                    'id'
                )
        }),
    )