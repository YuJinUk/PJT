from django.db import models

# Create your models here.
class MovieModel(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField(default=0)
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.CharField(max_length=50)
    description = models.TextField()
    actor_image = models.ImageField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째 글 - {self.title} {self.description}'
    
