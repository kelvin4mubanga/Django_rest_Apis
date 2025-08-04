
from rest_framework import generics
from .models import CoffeeProduct,CoffeeOrder
from .serializers import *
 #CoffeeProductSerializer,CoffeeOrderSerializer




class CoffeeProductList(generics.ListCreateAPIView):

    queryset =CoffeeProduct.objects.all()
    serializer_class=CoffeeProductSerializer

class CoffeeProductDetail(generics.ListCreateAPIView):

    queryset =CoffeeProduct.objects.all()
    serializer_class=CoffeeProductSerializer




class CoffeeOrderList(generics.ListCreateAPIView):

    queryset =CoffeeProduct.objects.all()
    serializer_class=CoffeeOrderSerializer

class CoffeeOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=CoffeeOrder.objects.all()
    serializer_class=CoffeeOrderSerializer
