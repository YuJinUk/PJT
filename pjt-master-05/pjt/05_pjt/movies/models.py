from django.db import models

# Create your models here.

class MovieModel(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null = True)

    def __str__(self):
        return f'{self.id}번째 글 - {self.title} {self.description}'
    