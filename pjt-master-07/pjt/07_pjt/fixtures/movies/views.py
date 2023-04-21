from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, MovieListSerializer, ReviewListSerializer, MovieDetailSerializer, ReviewsetSerializer

# Create your views here.

@api_view(['GET'])
def actors_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorListSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def reviews_list(request):
    reviews = Review.objects.all()
    serializer = ReviewsetSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        context = {
            "delete" : "review {} is deleted".format(review_pk)
        }
        return Response(context)
    else:
        serializer = ReviewListSerializer(review, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        
        
@api_view(['POST'])
def create_reviews(request, movie_pk):
    movies = Movie.objects.get(pk = movie_pk)
    serializer = ReviewListSerializer(data = request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie = movies)
        print(serializer)
        return Response(serializer.data)