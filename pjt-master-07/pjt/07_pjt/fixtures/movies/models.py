from django.db import models


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
    movie_id = models.ForeignKey("Movie", on_delete = models.CASCADE)