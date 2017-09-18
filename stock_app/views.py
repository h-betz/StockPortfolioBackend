"""
Some DRF stuff
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Stock
from .serializers import StockSerializer

# Create your views here.
class StockList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        stock = self.get_object(pk)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)