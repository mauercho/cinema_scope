from rest_framework import serializers
from .models import Profile, User
from movies.models import Movie, Review
from movies.serializers import MovieSimpleSerializer, ReviewSerializer
from django.conf import settings



class ProfileSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        favorites = MovieSimpleSerializer(many=True, read_only=True)
        like_movies = MovieSimpleSerializer(many=True, read_only=True)

        class ReviewListSerializer(serializers.ModelSerializer):
            class MovieTitleSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Movie
                    fields = ('title',)
            movie = MovieTitleSerializer(read_only=True)

            class Meta:
                model = Review
                fields = '__all__'
        review_set = ReviewListSerializer(many=True, read_only=True)

        class Meta:
            model = User
            fields = ('username', 'favorites', 'like_movies', 'review_set')
    user = UserSerializer(read_only=True)


    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user',)
