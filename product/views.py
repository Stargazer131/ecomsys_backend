from rest_framework import generics
from product.models import Product
from product.serializers import ProductSerializer
from django.db.models import Q
# Create your views here.


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
