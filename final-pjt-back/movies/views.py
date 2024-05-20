from django.shortcuts import render
from .models import Movie
from django.contrib.auth import get_user_model
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response


# Create your views here.
# 영화 리스트 조회
@api_view(['GET'])
def list(request):
    movies = Movie.objects.filter(id__lt=100)
    serializer = MovieSerializer(movies, many=True)
    # return Response(serializer.data)
    return JsonResponse(serializer.data, safe=False)


# 단일 영화 디테일 조회
@api_view(['GET'])
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data)


# 영화에 대해 좋아요 누르기
@api_view(['POST'])
def movie_likes(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)

    # like_user = request.user
    # like_movies = like_user.like_movies.all()

    # movielikes = Movielike.objects.get(like_user_id=request.user)
    # print(movielikes)
    # print(movielikes.movie.all())

    # if movie in like_movies.movielike_set.filter(likeability=1):
    #     # print(like_movies)
    #     print('좋아요 빼기')

    # if request.user in movielikes.like_user.all():
    # movie.like_users.remove(request.user)
    # print('좋아요 빼기')
    # else:
        # movielike = Movielike(movie=movie, like_user=request.user, likeability=1)
        # movielike.save()
        # print('좋아요 누르기')


    return JsonResponse({ 'like': 'OK' })