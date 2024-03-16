from rest_framework import serializers
from book.models import Book, Genre, Author, Publisher
from product.serializers import ProductSerializer


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
        
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    genres = GenreSerializer(many=True)
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    
    
    class Meta:
        fields = '__all__'
        model = Book
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context', {})
        self.fields['product'] = ProductSerializer(context=context)  # ProductSerializer with context


