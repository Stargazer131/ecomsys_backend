from django.urls import path
from order import views


urlpatterns = [
    path('create/', views.PlaceOrderAPIView.as_view(), name='place_order'),
]