from rest_framework import serializers

from apps.payments.models import Currency, Payment


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['code', 'name']


class CreatePaymentSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = CurrencySerializer()
    comment = serializers.CharField(allow_blank=True, required=False)
    recipient_card_number = serializers.CharField(max_length=16)


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['id', 'amount', 'currency', 'comment', 'recipient_card_number']