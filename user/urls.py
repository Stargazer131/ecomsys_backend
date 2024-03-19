from django.urls import path
from user import views


urlpatterns = [    
    path('login/', views.UserLoginAPIView.as_view(), name='user_login'),
    path('register/', views.UserRegisterAPIView.as_view(), name='user_register'),
]

