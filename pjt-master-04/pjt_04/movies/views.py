from django.shortcuts import render, redirect
from .models import MovieModel
from .forms import MovieForms
# Create your views here.

def index(request):
    movie = MovieModel.objects.all()
    context = {
        'movies' : movie,
    }
    return render(request, 'movies/index.html', context)
    
    
def detail(request, pk):
    print('detail')
    movie = MovieModel.objects.get(pk = pk)
    if request.method == "POST":
        form = MovieForms(request.POST, request.FILES, instance = movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk = movie.pk)
    else:
        form = MovieForms()
    context = {
        'movie' : movie,
        'form' : form
    }
    return render(request, 'movies/detail.html', context)

def create(request): # DB에 저장
    if request.method == 'POST':
        form = MovieForms(request.POST, request.FILES)
        if form.is_valid():
            print('hello')
            print(form.cleaned_data)
            form.save()
            return redirect('movies:index')
        # return redirect('movies:index')
    else:
        form = MovieForms()
    context = {
        'form' : form
    }
    return render(request, 'movies/create.html', context)

def update(request, pk):
    movie = MovieModel.objects.get(pk = pk)
    print('update')
    if request.method == 'POST':
        form = MovieForms(request.POST, instance=movie)
        if form.is_valid():
            form.save()
        return redirect('movies:index')
    else:
        form = MovieForms(instance=movie)
    context = {
        'form' : form,
        'movie' : movie,
    }    
    return render(request, 'movies/update.html', context)

    
def delete(request, pk):
    if request.method == "POST":
        movie = MovieModel.objects.get(pk = pk)
        movie.delete()
        return redirect('movies:index')