from django.contrib import admin

from .models import Administrativo


@admin.register(Administrativo)
class AdministrativoAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'nome', 'cpf', 'telefone')
    search_fields = ('nome', 'cpf')
    list_filter = ('nome', 'cpf')
    readonly_fields = ('uuid', 'id')

    fieldsets = (
        ('', {
            'fields':
                (
                    'nome',
                    'cpf',
                    'rg',
                    'sexo',
                    'tipo_logradouro',
                    'logradouro',
                    'numero',
                    'bairro',
                    'complemento',
                    'cep',
                    'telefone',
                    'data_de_nascimento',
                    'email',
                    'descricao',
                    'uuid',
                    'id'
                )
        }),
    )