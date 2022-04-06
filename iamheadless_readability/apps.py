import nltk
from django.apps import AppConfig


nltk.download('cmudict')
nltk.download('punkt')


class IamheadlessReadabilityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iamheadless_readability'
