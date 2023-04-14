from django.contrib import admin
from .models import MovieModel
# Register your models here.

# class MovieAdmin(admin.ModelAdmin):
#     pass

admin.site.register(MovieModel)