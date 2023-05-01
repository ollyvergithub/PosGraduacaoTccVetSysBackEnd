from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import Administrativo, Veterinario, Dependente


@admin.register(Dependente)
class DependenteAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'nome', 'sexo', 'data_de_nascimento', 'funcionario')
    search_fields = ('nome',)
    list_filter = (
        'nome',
        'sexo',
        ('data_de_nascimento', DateRangeFilter),
        'funcionario'
    )
    readonly_fields = ('uuid', 'id')

    fieldsets = (
        ('', {
            'fields':
                (
                    'nome',
                    'data_de_nascimento',
                    'sexo',
                    'funcionario',
                    'uuid',
                    'id'
                )
        }),
    )


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


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
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
                    'crmv',
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