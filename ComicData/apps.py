from django.apps import AppConfig


class ComicdataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ComicData'

    def ready(self):
        import ComicData.signals