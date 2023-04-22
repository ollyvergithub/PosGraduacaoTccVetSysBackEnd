from django.contrib import admin

from .models import Administrativo, Veterinario


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