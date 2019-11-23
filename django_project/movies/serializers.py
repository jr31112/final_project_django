from rest_framework import serializers
from .models import Movie, Genre, People

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class PeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['ko_name', 'en_name', 'birthday', 'gender', 'is_alive', 'popularity', 'place_of_birth', 'img_url']

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'overview', 'release_date', 'img_url', 'country', 'rating', 'popularity']

class MovieUpdateSerializers(serializers.ModelSerializer):
    # actors_set = PeopleSerializers(many=True)
    director_set = PeopleSerializers()
    genres_set = GenreSerializers(many=True)
    class Meta:
        model =  Movie
        fields = MovieSerializers.Meta.fields + ['genres_set'] + ['director_set']