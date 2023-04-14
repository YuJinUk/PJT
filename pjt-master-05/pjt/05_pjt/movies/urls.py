from django.urls import path, include
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('<pk>/', views.detail, name = 'detail'),
    path('<pk>/update', views.update, name = 'update'),
    path('<pk>/delete', views.delete, name = 'delete'),
]
