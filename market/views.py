from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from .models import CustomUser
from .serializers import CustomUserSerializers

class Register(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
    parser_classes = [MultiPartParser, FormParser]
