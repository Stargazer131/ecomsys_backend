from django.urls import path
from search import views


urlpatterns = [
    path('', views.SearchByNameAPIView.as_view(), name='search'),
]

