from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse

# Create your views here.
# 프로필 생성/수정/조회
@api_view(['GET', 'POST', 'PUT'])
def profile(request, user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    profile = Profile.objects.get(pk=user_pk)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=person)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=person)
            return JsonResponse(serializer.data)
