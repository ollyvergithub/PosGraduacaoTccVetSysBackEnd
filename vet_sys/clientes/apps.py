from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClientesConfig(AppConfig):
    name = "vet_sys.clientes"
    verbose_name = _("Clientes")
