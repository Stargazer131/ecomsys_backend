from django.urls import path
from search.views import search_by_name


urlpatterns = [
    path('', search_by_name, name='search'),
]

