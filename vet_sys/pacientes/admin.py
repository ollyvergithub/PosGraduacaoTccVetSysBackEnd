from django.contrib import admin

from .models import Especie, Raca, Porte, Paciente


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'nome', 'descricao')
    search_fields = ('nome',)
    list_filter = ('nome',)
    readonly_fields = ('uuid', 'id')
    fieldsets = (
        ('', {
            'fields':
                (
                    'nome',
                    'descricao',
                    'uuid',
                    'id'
                )
        }),
    )


@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'nome', 'descricao')
    search_fields = ('nome',)
    list_filter = ('nome',)
    readonly_fields = ('uuid', 'id')
    fieldsets = (
        ('', {
            'fields':
                (
                    'nome',
                    'descricao',
                    'uuid',
                    'id'
                )
        }),
    )


@admin.register(Porte)
class PorteAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'porte', 'descricao')
    search_fields = ('porte',)
    list_filter = ('porte',)
    readonly_fields = ('uuid', 'id')
    fieldsets = (
        ('', {
            'fields':
                (
                    'porte',
                    'descricao',
                    'uuid',
                    'id'
                )
        }),
    )


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'nome', 'especie', 'raca', 'porte')
    search_fields = ('nome',)
    list_filter = ('nome',)
    readonly_fields = ('uuid', 'id')

    fieldsets = (
        ('', {
            'fields':
                (
                    'nome',
                    'especie',
                    'raca',
                    'porte',
                    'sexo',
                    'tutor',
                    'data_nasc',
                    'pelagem',
                    'cor',
                    'descricao',
                    'uuid',
                    'id'
                )
        }),
    )