# serializers.py
from rest_framework import serializers
from .models import Genre, Movie, Series, Episode, Music

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class SeriesSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Series
        fields = '__all__'

class EpisodeSerializer(serializers.ModelSerializer):
    series = SeriesSerializer(read_only=True)

    class Meta:
        model = Episode
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Music
        fields = '__all__'
