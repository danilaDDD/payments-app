from django.urls import path

from apps.payments import views

app_name = 'payments'

urlpatterns = [
    path('payments/', views.CreatePaymentAPIView.as_view(), name='create_payment'),
]