from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import UserSerializer,WorkSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from . models import CustomUser,Work

# Create your views here.

# @api_view(['POST'])
# def signup_view(request):
#     if request.method == "POST":
#         username = request.data.get("username")
#         password = request.data.get("password")
#         email = request.data.get('email')

#         try:
#             user = User.objects.create_user(username=username,password=password,email=email)
#             if user:
#                 return Response({'message':'User logged in successfully!!'},status=status.HTTP_201_CREATED)
#         except IntegrityError as e:
#             return Response({'message':'Username already exists.'},status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"message":"Unable to create user."},status=status.HTTP_406_NOT_ACCEPTABLE)
    
class UserView(viewsets.ModelViewSet):
   
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    class Meta:
        model = CustomUser
        fields = '__all__'


class WorkList(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    class Meta:
        model = Work
        fields = '__all__'