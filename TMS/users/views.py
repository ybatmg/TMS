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