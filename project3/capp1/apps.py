from django.apps import AppConfig


class Capp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'capp1'
    
    def ready(self):
        import capp1.signals