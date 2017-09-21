"""
Some DRF stuff
"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from .controller import Controller

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
    def get_object(self, name):
        try:
            stock = Stock.objects.get(name=name)
            controller = Controller()
            stock_data = controller.get_ticker_data(stock.name)
            print(stock_data)
            return Stock.objects.get(name=name)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        stock = self.get_object(name)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        stock = self.get_object(name)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        stock = self.get_object(name)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # queryset = Stock.objects.all()
    # serializer_class = StockSerializer
    # lookup_field = 'name'  
    # def get(self, request, *args, **kwargs):
    #     stock = self.retrieve(request, *args, **kwargs)
    #     print("Stock " + stock)
    #     return stock
    #     #return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)  