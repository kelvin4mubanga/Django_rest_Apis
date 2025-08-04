
from rest_framework import generics

from .models import Vehicle,Reservation 

from .serializers import VehicleSerializer,ReservationSerializer

#Vihicles Views
class VehicleListView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer



class VehicleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset= Vehicle.objects.all()
    serializer_class = VehicleSerializer




#Reservation Views
class ReservationListView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer



class ReservationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset= Reservation.objects.all()
    serializer_class = ReservationSerializer