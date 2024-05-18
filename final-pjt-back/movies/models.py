from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, blank=True, related_name="movies")
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    vote_average = models.FloatField()
    release_date = models.DateField()
    poster_path = models.TextField()
    tmdb_id = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="like_movies")

    def __str__(self):
        return self.title