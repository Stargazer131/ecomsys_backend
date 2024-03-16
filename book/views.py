from rest_framework import generics
from book.models import Book
from book.serializers import BookSerializer
from django.db.models import Q


class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer