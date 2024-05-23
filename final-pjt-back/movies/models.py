from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, blank=True, related_name="movies")
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    vote_average = models.FloatField()
    release_date = models.DateField()
    poster_path = models.TextField(null=True)
    tmdb_id = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_movies')
    favorite_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='favorites')

# 영화에 대해 좋아요/별로예요 표시
# class Movielike(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     like_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     likeability = models.IntegerField()

# 영화에 달린 리뷰
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_reviews')
    content = models.TextField()