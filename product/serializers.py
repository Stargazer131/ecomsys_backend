from rest_framework import serializers
from product.models import Book, Genre, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre


class BookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)  # Use the GenreSerializer here
    
    class Meta:
        fields = '__all__'
        model = Book


