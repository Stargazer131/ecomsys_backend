from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from product.serializers import ProductSerializer


class SearchByNameAPIView(APIView):
    def post(self, request, *args, **kwargs):
        search_type = request.data.get('searchType')
        text_search = request.data.get('textSearch')
        image_search = request.data.get('imageSearch')
        voice_search = request.data.get('voiceSearch')

        if search_type == 'text':
            products = Product.objects.filter(name__icontains=text_search)
        elif search_type == 'voice':
            products = Product.objects.filter(name__icontains=voice_search)
        else:
            products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)

        response_data = {
            'products': serializer.data,
            'search_type': search_type,
        }

        return Response(response_data, status=status.HTTP_200_OK)