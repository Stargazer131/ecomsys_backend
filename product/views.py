from django.shortcuts import render
from rest_framework import generics
from product.models import Book, Genre, Product
from product.serializers import BookSerializer, GenreSerializer, ProductSerializer
from django.db.models import Q
# Create your views here.


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    
    # def get_queryset(self):
    #     return Genre.objects.filter(Q(slug=self.kwargs['slug']))


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    
    
class AllProductAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
      
def home(request):
    # Your data goes here
    products = Product.objects.all()  # Replace with your actual queryset

    # Pass data to the template
    context = {
        'products': products,
        # Add more variables as needed
    }

    # Render the template with the provided data
    return render(request, 'product/home.html', context)