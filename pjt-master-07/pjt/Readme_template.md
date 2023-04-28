>  PJT 작성 시 주의!
> 
> * 절대로 코드만 복붙하지 않는다.
> * 후기는 적어도 3줄은 씁시다!
> * 교수님이 안 볼 것 같지만 다 뜯어 봅니다.
> * 제출 당일 23:59분 내로 제출 합시다!
> * readme 없으면 일주일간 박제할 예정입니다. 
>   * 물론 readme 작성도 결국 해주셔야 합니다. 

# 

# PJT 07

### 이번 pjt 를 통해 배운 내용

* 장고로 api를 통해 데이터를 제공해주는 것은 신기하고 재밌었습니다.

* 참조 / 역참조는 부족함을 느껴 복습을 다시 해야할 것 같습니다.

## A. 전체 배우 목록 제공

* 요구 사항 : 전체 배우 목록 제공

* 결과 : 전체 배우 목록을 한 화면에 list형식으로 보여줬습니다.

* 
* 
* 
  
  * 문제 접근 방법 및 코드 설명
  
  ```python
  여기에 관련 작성 코드 복붙!  
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
          model = Rfrom django.db import models
  
  
  # Create your models here.
  
  class Actor(models.Model):
      name = models.CharField(max_length=100)
      
      
  class Movie(models.Model):
      title = models.CharField(max_length=100)
      overview = models.TextField(null=True, blank=True)
      release_date = models.DateTimeField()
      poster_path = models.TextField(null = True, blank = True)
      actors = models.ManyToManyField(Actor, through = "MovieActor")
      
  class Review(models.Model):
      movie = models.ForeignKey("Movie", on_delete = models.CASCADE)
      title = models.CharField(max_length=100)
      content = models.TextField(null=True, blank=True)
  
  # 중계테이블을 만들면 actors=[6]를 받아올 수 있다.
  class MovieActor(models.Model):
      actor_id = models.ForeignKey("Actor", on_delete = models.CASCADE)
      movie_id = models.ForeignKey("Movie", on_from django.shortcuts import render, redirect
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
          serializer.save(movie = moviesfrom django.urls import path
  from . import views
  
  
  urlpatterns = [
      path('actors/', views.actors_list, name = 'actors_list'),
      path('actors/<int:actor_pk>/', views.actor_detail, name = 'actor_detail'),
      path('movies/', views.movies_list, name = 'movies_list'),
      path('movies/<int:movie_pk>/', views.movie_detail, name = 'movie_detail'),
      path('reviews/', views.reviews_list, name = 'reviews_list'),
      path('reviews/<int:review_pk>/', views.review_detail, name = 'review_detail'),
      path('movies/<int:movie_pk>/reviews/', views.create_reviews, name = 'create_reviews'),
  ])
          print(serializer)
          return Response(serializer.data)delete = models.CASCADE)eview
          fields = '__all__'
          
          
  
  ```
  
  * 이 문제에서 어려웠던점
  * 내가 생각하는 이 문제의 포인트

-----

....

문제 푼 내용을 기반으로 적어주세요.

# 후기

* 오늘 프로젝트는 쉬워 보였지만 나의 착각이었다.
* 고수가 되기 위해 오늘도 난 매진한다!
* 일단 롤 한판 하고... 
* 라고 생각만 하고 열공해야겠다!
