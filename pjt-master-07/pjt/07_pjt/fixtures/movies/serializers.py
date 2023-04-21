from rest_framework import serializers
from .models import Actor, Movie, Review, MovieActor

# Actor detail용 child
class Movietitle(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

# Movie main용
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','overview',)

# Actor detail용 parent
class ActorListSerializer(serializers.ModelSerializer):
    movies = Movietitle(many=True, read_only=True, source='movie_set')
    class Meta:
        model = Actor
        fields = ('id', 'movies','name',)

# Movie detail용 child
class ActorchildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)

# Movie detail용 child
class ReviewsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title','content',)

# Movie detail용 parent
class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorchildSerializer(many=True)
    review_set = ReviewsetSerializer(many = True)
    class Meta:
        model = Movie
        fields = '__all__'

# Review detail용 child
class ReviewchildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

# Review main용
class ReviewListSerializer(serializers.ModelSerializer):
    movie = ReviewchildSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        
        
