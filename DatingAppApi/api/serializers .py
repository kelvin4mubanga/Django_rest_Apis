from rest_framework import serializers
from .models import DatingProfile,Match

# Dating app serializers
class DatingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatingProfile
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
