
from rest_framework import serializers
from .models import CoffeeProduct,CoffeeOrder

# Coffee shop app serializers
class CoffeeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeProduct
        fields = '__all__'

class CoffeeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeOrder
        fields = '__all__'
