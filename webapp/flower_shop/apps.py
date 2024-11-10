from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FlowerShopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "flower_shop"
    verbose_name = _("Клуб единоборств")
