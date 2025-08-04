from rest_framework import serializers
from .models import Vehicle,Reservation


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        
        fields=('id','name','vehicle_type','registration_number','availability',)
        model=Vehicle




class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        
        fields=('id','user','vehicle','start_date','end_date','created_at')
        model=Reservation