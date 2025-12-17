from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

from apps.accounts.views import RegistrationAPIView, GetAccountsAPIView, GetAccountByIdAPIView

app_name = 'accounts'

urlpatterns = [
    path('accounts/', GetAccountsAPIView.as_view(), name='get_accounts'),
    path('accounts/<int:account_id>/', GetAccountByIdAPIView.as_view(), name='get_account_by_id'),
    path('accounts/', RegistrationAPIView.as_view(), name='registration'),
    path('tokens/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokens/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tokens/verify/', TokenVerifyView.as_view(), name='token_verify'),
]