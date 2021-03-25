from django.apps import AppConfig


class BlogpartConfig(AppConfig):
    name = 'BlogPart'

    def ready(self):
        import BlogPart.signals

