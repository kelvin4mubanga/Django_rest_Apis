from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        
        fields=('id','title','body','created_at',)
        model= Todo