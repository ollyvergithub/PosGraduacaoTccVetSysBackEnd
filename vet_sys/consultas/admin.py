from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import Consulta


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'data_da_consulta', 'paciente', 'cliente', 'veterinario')
    search_fields = ('paciente',)
    list_filter = (
        'paciente',
        'cliente',
        'veterinario',
        ('data_da_consulta', DateRangeFilter),
    )
    readonly_fields = ('uuid', 'id')
