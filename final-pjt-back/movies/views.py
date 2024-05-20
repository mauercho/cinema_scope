from django.shortcuts import render
from .models import Movie
from django.contrib.auth import get_user_model
from .serializers import MovieSerializer, ReviewSerializer
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


# fav 선택
@api_view(['POST'])
def favorites(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user in movie.favorite_users.all():
        movie.favorite_users.remove(request.user)
        is_favorite = False
        print('favorite 삭제')
    else:
        movie.favorite_users.add(request.user)
        is_favorite = True
        print('favorite 추가')
    return JsonResponse({'is_favorite': is_favorite})





###### 영화별 리뷰(코멘트) 관련 #######
@api_view(['GET', 'POST'])
def reviews(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        pass