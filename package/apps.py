from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PackageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "package"
    verbose_name = _("Package")
