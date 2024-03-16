from django.urls import path
from book import views


urlpatterns = [
    path('all/', views.BookListAPI.as_view(), name='book_list'),
]

