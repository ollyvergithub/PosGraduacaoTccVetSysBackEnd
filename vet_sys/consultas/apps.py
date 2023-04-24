from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ConsultasConfig(AppConfig):
    name = "vet_sys.consultas"
    verbose_name = _("Consultas")
