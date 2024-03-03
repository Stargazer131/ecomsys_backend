from django.urls import path
from cart import views


urlpatterns = [
    path('', views.CartListAPIView.as_view(), name='cart_list'),
]

