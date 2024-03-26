from rest_framework import serializers
from order.models import Order
# from user.serializers import UserSerializer  # Assuming you have a User model and its serializer


class OrderSerializer(serializers.ModelSerializer):
    # user = UserSerializer()  # Assuming UserSerializer is defined
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'created_timestamp', 'total_price']
