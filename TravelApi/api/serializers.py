# serializers.py
from rest_framework import serializers
from .models import Destination, TravelPackage, Booking, Review

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class TravelPackageSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer(read_only=True)

    class Meta:
        model = TravelPackage
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    travel_package = TravelPackageSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    destination = DestinationSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
