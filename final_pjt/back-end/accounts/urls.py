from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user-list'),
    path('users/<str:username>', views.user_profile),
    path('users/nickname', views.user_nickname, name='user-nickname'),
    # path('users/login/', views.login),
]
