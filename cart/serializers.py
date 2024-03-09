from rest_framework import serializers
from cart.models import CartItem
from product.models import Product
from product.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        product_id = representation['product_id']

        # Assuming ProductSerializer is defined as before
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(product, context=self.context)
        representation['product'] = product_serializer.data

        return representation

