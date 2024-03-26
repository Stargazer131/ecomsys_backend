from django.urls import path
from shipment import views


urlpatterns = [
    path('method/all/', views.ShipmentMethodListAPIView.as_view(), name='shipment_method_list'),
]