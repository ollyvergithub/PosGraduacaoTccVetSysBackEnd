from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PessoaConfig(AppConfig):
    name = "vet_sys.pessoas"
    verbose_name = _("Pessoas")