#/storage/emulated/0/python/web_course/DjangoApps/PropertyRentalApi

# Create your views here.
from .models import Property, PropertyCategory,Booking,Review
from .serializers import PropertySerializer,BookingSerializer,ReviewSerializer,PropertyCategorySerializer


from rest_framework import generics


#Travel API destination views start
class PropertyList(generics.ListCreateAPIView):

    queryset =Property.objects.all()
    serializer_class=PropertySerializer

class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    
     queryset =Property.objects.all()
     serializer_class=PropertySerializer

#Travel API destination views end
#Travel API travel package views start
class PropertyCategoryList(generics.ListCreateAPIView):

    queryset =PropertyCategory.objects.all()
    serializer_class= PropertyCategorySerializer

class PropertyCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    
     queryset =PropertyCategory.objects.all()
     serializer_class= PropertyCategorySerializer
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