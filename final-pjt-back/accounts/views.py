from django.shortcuts import render
from .models import Profile
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def profile(request, user_pk):
    profile = Profile.objects.get(pk=user_pk)