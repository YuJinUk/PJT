from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Accounts(AbstractUser):
    # genres = models.CharField(max_length=255, default='Actions')
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    nickname = models.CharField(max_length=255)
    profile_img = ProcessedImageField(
        upload_to='profile_images/', 
        null=True,
        blank=True,
        processors=[ResizeToFill(100,100)],
        options={'quality':70},
        )
    
    def __str__(self):
        return self.username