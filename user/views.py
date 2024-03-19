from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from django.utils.text import slugify
# from user.serializers import UserSerializer


class UserLoginAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pass
    
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username, password=password)
            user_id = user.id
        except User.DoesNotExist:
            user_id = -1
        
        response_data = {
            'user_id': user_id
        } 
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    
class UserRegisterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pass
    
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        birthday = request.POST.get('birthday')
        email = request.POST.get('email')
        slug = slugify(username)
        birthday_date = datetime.strptime(birthday, '%Y-%m-%d').date()
        
        try:
            user = User.objects.get(username=username)
            response_data = {
                'success': False
            } 
            
        except User.DoesNotExist:
            user = User(
                username=username, email=email, slug=slug,
                password=password, birthday=birthday_date
            )
            user.save()
            response_data = {
                'success': True
            } 
        
        return Response(response_data, status=status.HTTP_200_OK)