from django.contrib import admin

from apps.payments.models import Currency, Payment


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'created_at', 'updated_at']
    search_fields = ['code', 'name']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('code', 'name', 'created_at', 'updated_at')}),
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('amount', 'currency', 'comment', 'recipient_card_number')}),
        (None, {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ['created_at', 'updated_at']
    raw_id_fields = ['currency']
    list_display = ['amount', 'currency', 'recipient_card_number',]