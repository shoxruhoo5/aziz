from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializers

class Register(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
    parser_classes = [MultiPartParser, FormParser]
class MyTokenView(APIView):  
    def post(self,request): 
        username = request.data['username'] 
        password = request.data['password']
        user = CustomUser.objects.filter(username=username).last() 
        if user: 
            if user.check_password(password): 
                tokens=RefreshToken.for_user(user=user) 
                message =({ 
                    "username": user.username, 
                    "status": user.status, 
                    "refresh": str(tokens), 
                    "access": str(tokens.access_token), 
                    "user_id": user.id, 
                }) 
                return Response(message) 
            return Response({ 
                'message':'Password is invalid....' 
            }) 
        return Response({ 
                'message':'Username or Password is invalid....' 
            })


