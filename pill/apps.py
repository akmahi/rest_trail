from django.apps import AppConfig


class PillConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pill'

    def ready(self):
        import pill.signals

