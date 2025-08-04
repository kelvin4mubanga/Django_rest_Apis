from .models import AuctionCategory, AuctionItem, Bid

from .serializers import AuctionCategorySerializer, AuctionItemSerializer, BidSerializer




from rest_framework import generics


#auction  API  auctionitem views start
class AuctionItemList(generics.ListCreateAPIView):

    queryset =AuctionItem.objects.all()
    serializer_class=AuctionItemSerializer

class AuctionItemDetail(generics.RetrieveUpdateDestroyAPIView):
    
     queryset =AuctionItem.objects.all()
     serializer_class=AuctionItemSerializer



# auction API AuctionCategory views start
class AuctionCategoryList(generics.ListCreateAPIView):

    queryset =AuctionCategory.objects.all()
    serializer_class=AuctionCategorySerializer

class AuctionCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    
     queryset =AuctionCategory.objects.all()
     serializer_class=AuctionCategorySerializer



#Auction API Bid views start
class BidList(generics.ListCreateAPIView):

    queryset =Bid.objects.all()
    serializer_class=BidSerializer

class BidDetail(generics.RetrieveUpdateDestroyAPIView):
    
     queryset =Bid.objects.all()
     serializer_class=BidSerializer
