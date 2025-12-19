import pytest

@pytest.mark.django_db
class TestDBOperations:
    def test_insert_account(self):
        from apps.accounts.models import Account

        Account.objects.create(username='testuser', password='testpass')
        assert Account.objects.count() == 1
