import nltk
from django.apps import AppConfig


nltk.download('cmudict')


class IamheadlessReadabilityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iamheadless_readability'
