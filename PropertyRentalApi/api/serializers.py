from rest_framework import serializers
from .models import PropertyCategory, Property, Booking, Review

class PropertyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyCategory
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    category = PropertyCategorySerializer(read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Property
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
