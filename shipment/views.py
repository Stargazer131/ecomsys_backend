from rest_framework.views import APIView
from rest_framework.response import Response
from shipment.models import Shipment
from rest_framework import status
from django.conf import settings


# Create your views here.
class ShipmentMethodListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        response_data = {
            'shipping_choices': Shipment.shipping_methods
        }

        return Response(response_data, status=status.HTTP_200_OK)
