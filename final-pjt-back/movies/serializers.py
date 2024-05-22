from rest_framework import serializers
from .models import Movie, Genre, Review
from accounts.models import Profile, User




class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'tmdb_id')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    
    class ReviewUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)
    username = ReviewUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie')
