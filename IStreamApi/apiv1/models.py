# models.py
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.DurationField()
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.SET_NULL, null=True)
    director = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    poster_image = models.ImageField(upload_to='posters/')
    
    def __str__(self):
        return self.title

class Series(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, related_name='series', on_delete=models.SET_NULL, null=True)
    number_of_seasons = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    poster_image = models.ImageField(upload_to='posters/')
    
    def __str__(self):
        return self.title

class Episode(models.Model):
    series = models.ForeignKey(Series, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    season_number = models.IntegerField()
    episode_number = models.IntegerField()
    duration = models.DurationField()
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title} - S{self.season_number}E{self.episode_number}"

class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, null=True, blank=True)
    genre = models.ForeignKey(Genre, related_name='music', on_delete=models.SET_NULL, null=True)
    release_date = models.DateField()
    duration = models.DurationField()
    file = models.FileField(upload_to='music/')

    def __str__(self):
        return self.title

