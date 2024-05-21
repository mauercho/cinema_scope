from rest_framework import serializers
from .models import Profile, User
from movies.serializers import MovieSimpleSerializer, ReviewSerializer
from django.conf import settings



class ProfileSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        favorites = MovieSimpleSerializer(many=True, read_only=True)
        like_movies = MovieSimpleSerializer(many=True, read_only=True)
        review_set = ReviewSerializer(many=True, read_only=True)
        class Meta:
            model = User
            fields = ('favorites', 'like_movies', 'review_set')
    user = UserSerializer(read_only=True)


    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user',)
