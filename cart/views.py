from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cart import cart
from cart.models import CartItem
from cart.serializers import CartItemSerializer


class CartListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cart_id = request.GET.get(cart.CART_ID_SESSION_KEY)
        if cart_id is None:
            response_data = {
                cart.CART_ID_SESSION_KEY: cart.generate_cart_id()
            }

        else: 
            cart_items = CartItem.objects.filter(cart_id=cart_id)            
            serializer = CartItemSerializer(cart_items, many=True)
            response_data = {
                'cart_items': serializer.data
            }
            

        return Response(response_data, status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        action = request.data.get('action')
        cart_id = request.data.get(cart.CART_ID_SESSION_KEY)
        
        if action == 'add':
            product_id = request.data.get('product_id')
            cart.add_to_cart(product_id, cart_id)
        elif action == 'update':
            cart_item_id = request.data.get('cart_item_id')
            quantity = request.data.get('quantity')            
            cart.update_cart(cart_item_id, quantity)
        else:
            cart_item_id = request.data.get('cart_item_id')
            cart.remove_from_cart(cart_item_id)
        
        cart_items = CartItem.objects.filter(cart_id=cart_id)            
        serializer = CartItemSerializer(cart_items, many=True)
        response_data = {
            'cart_items': serializer.data
        } 
        
        return Response(response_data, status=status.HTTP_200_OK)