from rest_framework import serializers
from product.models import Book, Genre, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre


class BookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)  # Use the GenreSerializer here
    
    class Meta:
        model = Book


