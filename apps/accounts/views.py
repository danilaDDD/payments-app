from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.accounts.models import Account
from apps.accounts.permissions import PrimaryAccessPermission
from apps.accounts.serializers import AccountSerializer, AccountListSerializer


# Create your views here.
class RegistrationAPIView(GenericAPIView):
    serializer_class = AccountSerializer
    permission_classes = [PrimaryAccessPermission]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAccountsAPIView(GenericAPIView):
    serializer_class = AccountListSerializer
    permission_classes = [PrimaryAccessPermission]
    http_method_names = ['get']

    def get(self, request: Request):
        accounts = Account.objects.filter(is_active=True, is_staff=False)

        chat_id: int | None= request.query_params.get('chat-id')
        if chat_id is not None:
            accounts = accounts.filter(chat_id=chat_id)

        serializer = self.serializer_class(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAccountByIdAPIView(GenericAPIView):
    serializer_class = AccountSerializer
    permission_classes = [PrimaryAccessPermission]
    http_method_names = ['get']

    def get(self, request: Request, account_id: int):
        account = Account.objects.filter(id=account_id, is_active=True).first()
        if not account:
            return Response({'detail': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(account)
        return Response(serializer.data, status=status.HTTP_200_OK)