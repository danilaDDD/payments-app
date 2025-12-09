from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.payments.serializers import CreatePaymentSerializer, PaymentSerializer


class CreatePaymentAPIView(CreateAPIView):
    serializer_class = CreatePaymentSerializer

    @swagger_auto_schema(
        tags=['payments'],
        operation_summary='Создание платежа',
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()

        return Response(PaymentSerializer(payment).data)

