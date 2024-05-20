from django.shortcuts import render, redirect
from .models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse

# Create your views here.
# 프로필 생성/수정/조회
@api_view(['GET', 'POST', 'PUT'])
def profile(request, user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    # 프로필이 아직 생성되지 않았을 때에는 None 값 할당
    try:
        profile = Profile.objects.get(pk=user_pk)
    except Profile.DoesNotExist:
        profile = None

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


@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
def follow(request, user_pk):
    me = request.user
    you = get_user_model().objects.get(pk=user_pk)


    if me != you:
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed = False
        else:
            you.followers.add(me)
            is_followed = True
        
        context = {
            'is_followed': is_followed,
            'followings_count': you.followings.count(),
            'followers_count': you.followers.count()
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.pk)