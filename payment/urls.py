from django.urls import path
from payment import views


urlpatterns = [
    path('method/all/', views.PaymentMethodListAPIView.as_view(), name='payment_method_list'),
]