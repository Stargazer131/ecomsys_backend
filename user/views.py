from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import User
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