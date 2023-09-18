from django.apps import AppConfig

from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layout="vertical"
    

class BoardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boards'
