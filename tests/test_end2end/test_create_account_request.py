import pytest

from apps.accounts.models import PrimaryAccess


class TestCreateAccountRequest:
    @pytest.mark.django_db
    @pytest.mark.urls('accounts.urls')
    def test_nothing(self, client, primary_access):
        primary_access.save()

        assert client is not None
        assert primary_access is not None
        assert PrimaryAccess.objects.count() == 1
