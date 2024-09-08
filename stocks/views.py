from rest_framework import generics
from .models import Stocks
from .serializers import StocksSerializer

class StocksListCreateView(generics.ListCreateAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer

class StocksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer
