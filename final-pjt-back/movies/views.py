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
    movie = Movie.objects.get(pk=movie_pk)

    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
        is_liked = False
        print('좋아요 취소')
    else:
        movie.like_users.add(request.user)
        is_liked = True
        print('좋아요')


    return JsonResponse({'is_liked': is_liked})