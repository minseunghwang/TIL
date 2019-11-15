from django.shortcuts import render
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movies_pk):
    movies = Movie.objects.get(pk=movies_pk)
    context ={
        'movies' : movies,
    }
    return render(request, 'movies/detail.html',context)

def create(request):
    form = MovieForm()
    context = {
        'form':form
        }
    return render(request, 'movies/create.html',context)