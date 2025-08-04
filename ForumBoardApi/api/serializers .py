from rest_framework import serializers
from .models import ForumThread,ForumPost


# Forum board app serializers
class ForumThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumThread
        fields = '__all__'

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = '__all__'
