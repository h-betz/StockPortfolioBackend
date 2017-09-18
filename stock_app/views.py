"""
Some DRF stuff
"""
from rest_framework import generics
from .models import Stock
from .serializers import StockSerializer

# Create your views here.
class StockList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer