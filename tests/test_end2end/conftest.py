import os

import pytest

from apps.accounts.models import PrimaryAccess, Account
from apps.payments.models import Payment


def clean_db():
    PrimaryAccess.objects.all().delete()
    Account.objects.all().delete()
    Payment.objects.all().delete()


@pytest.fixture(scope='session')
def primary_access() -> PrimaryAccess:
    return PrimaryAccess(owner='test', token='cwiebhceweuicbi', is_active=True)

