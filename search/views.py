from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from product.serializers import ProductSerializer
# from search.image_recommender import predict_similar_image


class SearchByNameAPIView(APIView):
    def post(self, request, *args, **kwargs):
        search_type = request.POST.get('searchType')
        text_search = request.POST.get('textSearch')
        image_search = request.FILES.get('imageSearch')
        voice_search = request.POST.get('voiceSearch')

        if search_type == 'text':
            products = Product.objects.filter(name__icontains=text_search)
        elif search_type == 'voice':
            products = Product.objects.filter(name__icontains=voice_search)
        else:
            similar_product_ids = []
            products = Product.objects.filter(id__in=similar_product_ids)

        serializer = ProductSerializer(products, many=True, context={"request": request})

        response_data = {
            'products': serializer.data,
            'search_type': search_type,
        }

        return Response(response_data, status=status.HTTP_200_OK)