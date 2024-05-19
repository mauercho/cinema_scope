from django.shortcuts import render
from .models import Movie
from django.contrib.auth import get_user_model
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def list(request):
    movies = Movie.objects.filter(id__lt=100)
    serializer = MovieSerializer(movies, many=True)
    # return Response(serializer.data)
    return JsonResponse(serializer.data, safe=False)