from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .serializers import UserRegisterSerializer, UserLoginSerializer, StocksSerializer
from .models import Stocks

# Stocks views remain unchanged
class StocksListCreateView(generics.ListCreateAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer

class StocksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
