from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "vet_sys.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import vet_sys.users.signals  # noqa F401
        except ImportError:
            pass
