from django.shortcuts import render, redirect
from .models import MovieModel
from .forms import MovieForm
# Create your views here.

def index(request):
    movie = MovieModel.objects.all()
    context = {
        'movies' : movie
    }
    return render(request, 'movies/index.html', context)

def create(request):
    print('!!!!!!!!!!!!!!!!!!!!!!!')
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
        return redirect('movies:index')
    else:
        form = MovieForm()
        context = {
            'form' : form
        }
        return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = MovieModel.objects.get(pk = pk)
    context = {
        'movies' : movie,
        'pk' : pk,
    }
    return render(request, 'movies/detail.html', context)


def update(request, pk):
    movie = MovieModel.objects.get(pk = pk)
    # if request.user == movie.user:
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance = movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk = movie.pk)
    else:
        form = MovieForm(instance = movie)
    context = {
        'form' : form,
        'movies' : movie
    }
    print(context)
    return render(request, 'movies/update.html', context)

def delete(request, pk):
    movie = MovieModel.objects.get(pk = pk)
    movie.delete()
    return redirect('movies:index')