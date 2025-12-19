import os
from pathlib import Path

import pytest
from django.conf import settings
from dotenv import load_dotenv


@pytest.fixture(scope='session')
def django_db_setup():
    """Configure the Django test database settings for end-to-end tests."""
    pass
