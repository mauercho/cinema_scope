from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import os
import openai
import requests
import re



# Create your views here.
# 메인 영화 리스트 조회
@api_view(['GET'])
def list(request):
    movies = Movie.objects.filter(id__lt=21)
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)




###### 단일 영화 관련 #######

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

# 특정 영화에 대한 리뷰 조회 / 생성
@api_view(['GET', 'POST'])
def reviews(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        

# 특정 리뷰 수정 / 삭제
@api_view(['DELETE', 'PUT'])
def review_detail(request, movie_pk, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.method == 'DELETE':
        print(review)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
        
# 리뷰 좋아요
@api_view(['POST'])
def review_likes(request, movie_pk, review_pk):
    movie = Movie.objects.get(pk=movie_pk)
    review = Review.objects.get(pk=review_pk)

    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        is_liked = False
        print('좋아요 취소')
    else:
        review.like_users.add(request.user)
        is_liked = True
        print('좋아요')
    return JsonResponse({'is_liked': is_liked})




openai.api_key = "sk-proj-Vg67oj0tLNOVqO4HeyoJT3BlbkFJHOSZXr9VRLoPofam5kd9"
###### 영화 추천 받기 ######
@csrf_exempt
def recommend(request, user_pk):
    try:
        user = get_user_model().objects.get(pk=user_pk)
    except get_user_model().DoesNotExist:
        return JsonResponse({'error': 'User not found.'}, status=404)

    liked_movies = user.like_movies.all()
    print(liked_movies)
    if not liked_movies.exists():
        return JsonResponse({'error': 'No liked movies found for the user.'}, status=400)

    liked_movie_titles = [movie.original_title for movie in liked_movies]
    prompt = generate_prompt(liked_movie_titles)
    
    # client = openai.OpenAI(api_key = "sk-proj-Vg67oj0tLNOVqO4HeyoJT3BlbkFJHOSZXr9VRLoPofam5kd9")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    recommendations_text = response.choices[0].message.content.strip()
    recommendations = recommendations_text.split('\n')
    recommendations = [rec.strip() for rec in recommendations if rec.strip()]
    print('recommendations', recommendations)
    print()
    print('이제진짜 제목', recommendations[3])




    # movie_titles = extract_movie_titles(recommendations)
    # print(movie_titles)



    tmdb_recommendations = []
    for movie_title in recommendations:
        print('title', movie_title)
        tmdb_data = get_tmdb_data(movie_title)
        if tmdb_data:
            tmdb_recommendations.append(tmdb_data)

    return JsonResponse({'recommendations': tmdb_recommendations})





def generate_prompt(liked_movies):
    liked_movies_str = ", ".join(liked_movies)
    prompt = (
        f"I have enjoyed the following movies: {liked_movies_str}. " +
        "Can you recommend me at least 5 similar movies that I might like? " +
        "Please provide the recommendations only 'title'."
    )
    print('prompt', prompt)
    return prompt




def get_tmdb_data(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': "047195d71080c8a4198669abf6149129",
        'query': movie_title,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(response.json())
        # results = response.json().get['results']
        # print("get_tmdb_data의", results)
        # if results:
        #     return results[0]  # return the first matching movie
    return None



# def extract_movie_titles(text):
#     # Define the regular expression pattern
#     pattern = r'"\s*(.*?)\s*"'  # matches anything within double quotes
    
#     # Find all matches
#     matches = re.findall(pattern, text)
    
#     # Remove leading and trailing whitespace from each match
#     movie_titles = [match.strip() for match in matches]
    
#     return movie_titles