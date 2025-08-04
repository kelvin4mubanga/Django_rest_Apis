from .models import Destination, TravelPackage, Booking, Review
from .serializers import DestinationSerializer,TravelPackageSerializer,BookingSerializer,ReviewSerializer


from rest_framework import generics


#Travel API destination views start
class DestinationList(generics.ListCreateAPIView):

    queryset =Destination.objects.all()
    serializer_class=DestinationSerializer

class DestinationDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset =Destination.objects.all()
     serializer_class=DestinationSerializer

#Travel API destination views end
#Travel API travel package views start
class TravelPackageList(generics.ListCreateAPIView):

    queryset =TravelPackage.objects.all()
    serializer_class= TravelPackageSerializer

class TravelPackageDetail(generics.RetrieveUpdateDestroyAPIView):
    
     queryset =TravelPackage.objects.all()
     serializer_class= TravelPackageSerializer
#Travel API travel package views end
#Travel API booking views start
class BookingList(generics.ListCreateAPIView):

    queryset =Booking.objects.all()
    serializer_class=BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset =Booking.objects.all()
    serializer_class=BookingSerializer
#Travel API booking views ends

#Travel API review views start
class ReviewList(generics.ListCreateAPIView):

    queryset =Review.objects.all()
    serializer_class=ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset =Review.objects.all()
    serializer_class=ReviewSerializer
#Travel API review views ends