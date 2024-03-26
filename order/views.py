from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from order.models import Order
from shipment.models import Shipment
from payment.models import Payment
from user.models import User
from cart import cart
from django.conf import settings


# Create your views here.
class PlaceOrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        user_id = request.POST.get(settings.USER_ID_KEY)

        shipping_address = request.POST.get("shipping_address")
        shipping_method = request.POST.get("shipping_method")

        payment_method = request.POST.get("payment_method")
        card_number = request.POST.get("card_number")
        expired_date = request.POST.get("expired_date")
        expired_date = datetime.strptime(expired_date, "%Y-%m-%d").date()
        security_code = request.POST.get("security_code")

        # process
        user = User.objects.get(id=user_id)
        cart_items = cart.get_cart_items(user_id)
        total_price = 0
        for item in cart_items:
            total_price += item.total_price

        # create order
        order = Order(user=user, status="Transporting", total_price=total_price)
        order.save()

        # update cart item
        for item in cart.get_cart_items(user_id):
            item.order = order
            item.save()

        # create shipment
        shipment = Shipment(
            order=order,
            shipping_address=shipping_address,
            shipping_method=shipping_method,
            tracking_information="On the way",
        )
        shipment.save()

        # create payment
        total_amount = float(total_price) + float(shipment.fee )
        payment = Payment(
            order=order,
            method=payment_method,
            status='Pending',
            card_number=card_number,
            expired_date=expired_date,
            security_code=security_code,
            paid_amount=0,
            total_amount=total_amount
        )
        payment.save()
        
        response_data = {
            'created_status': 'successfully'
        } 
        
        return Response(response_data, status=status.HTTP_200_OK)
