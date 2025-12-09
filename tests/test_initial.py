import os
from xml.dom.xmlbuilder import DOMBuilder

from django.conf import settings

from settings.settings import DATABASES


def test_env_variable():
    assert os.getenv('ENV') == 'test'


def test_settings_module():
    assert os.getenv('DJANGO_SETTINGS_MODULE') == 'settings.settings'
    assert settings is not None
    assert settings.ENV == 'test'

    DB_SETTINGS = settings.DATABASES['default']
    assert DB_SETTINGS['NAME'].startswith('test_')

