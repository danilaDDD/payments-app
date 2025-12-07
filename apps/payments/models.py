from django.db.models import DecimalField, ForeignKey
from django.db import models

from apps.common.models import AbsCreated

class Currency(AbsCreated):
    code = models.CharField('Код валюты', max_length=8, unique=True)
    name = models.CharField('Название валюты', max_length=64)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class Payment(AbsCreated):
    amount = models.DecimalField('Cумма выплаты', max_digits=10, decimal_places=2)
    currency = ForeignKey(Currency, on_delete=models.CASCADE, related_name='payments')
    comment = models.TextField('Комментарий', blank=True, null=True)
    recipient_card_number = models.CharField('Номер карты получателя', max_length=16)

    def __str__(self):
        return f'{self.amount} {self.currency.code} to {self.recipient_card_number}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
