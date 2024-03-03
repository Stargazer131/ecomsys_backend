from django.urls import path
from product import views


urlpatterns = [
    path('api/books/', views.BookListAPIView.as_view(), name='book_list'),
    path('api/genres/', views.GenreListAPIView.as_view(), name='genre_list'),
    path('api/genres/<slug:slug>/', views.GenreDetailAPIView.as_view(), name='genre_detail'),
    path('api/books/<slug:slug>/', views.BookDetailAPIView.as_view(), name='book_detail'),
    
    path('all/', views.AllProductAPI.as_view(), name='product_all'),
]

