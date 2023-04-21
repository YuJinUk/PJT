from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.actors_list, name = 'actors_list'),
    path('actors/<int:actor_pk>/', views.actor_detail, name = 'actor_detail'),
    path('movies/', views.movies_list, name = 'movies_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name = 'movie_detail'),
    path('reviews/', views.reviews_list, name = 'reviews_list'),
    path('reviews/<int:review_pk>/', views.review_detail, name = 'review_detail'),
    path('movies/<int:movie_pk>/reviews/', views.create_reviews, name = 'create_reviews'),
]