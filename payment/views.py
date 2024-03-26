from rest_framework.views import APIView
from rest_framework.response import Response
from payment.models import Payment
from rest_framework import status
from django.conf import settings


# Create your views here.
class PaymentMethodListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        response_data = {
            'payment_method_choices': Payment.payment_choice_list
        }

        return Response(response_data, status=status.HTTP_200_OK)
