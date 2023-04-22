from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FuncionariosConfig(AppConfig):
    name = "vet_sys.funcionarios"
    verbose_name = _("Funcionários")
