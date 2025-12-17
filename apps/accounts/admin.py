from django.contrib import admin

from apps.accounts.models import Account, PrimaryAccess


# Register your models here.
@admin.register(PrimaryAccess)
class PrimaryAccessAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at',]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'email', 'is_active', 'created_at', 'updated_at',)
    readonly_fields = ['password', 'created_at', 'updated_at',]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'patronymic', 'email',
                                         'phone', 'birth_date', 'gender', 'created_at', 'updated_at',)}),
        ('Security', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),

    )

