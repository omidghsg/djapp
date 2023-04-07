import inject
from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mainapp"

    def get_permissions_class(self):
        from mainapp.permissions import MainAppPermissions

        return MainAppPermissions

    def ready(self):
        from .di import di_config

        inject.configure_once(di_config)
