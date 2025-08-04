from django.contrib import admin

# Register your models here.
from .models import Genre, Movie, Series, Episode, Music
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(Episode)
admin.site.register(Music)