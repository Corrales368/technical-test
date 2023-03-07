from django.apps import AppConfig


class ExamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.exam'

    def ready(self) -> None:
        from . import signals
        return super().ready()
