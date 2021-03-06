from django.views.decorators.http import require_POST
from django.shortcuts import render,redirect, get_object_or_404
from .models import Movie, Comment
import csv

# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    print(movies[0].title)
    
    context ={
        'movies' : movies
    }
    return render(request, 'movies/index.html',context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.comment_set.all()
    context = {
        'movie' : movie,
        'comments' : comments,
    }
    return render(request, 'movies/detail.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grade = request.POST.get('watch_grade')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date,
    genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    movie.save()

    return redirect('/movies/')


@require_POST
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('/movies/')


def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/edit.html', context)


def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.title = request.POST.get('title')
    movie.title_en = request.POST.get('title_en')
    movie.audience = request.POST.get('audience')
    movie.open_date = request.POST.get('open_date')
    movie.genre = request.POST.get('genre')
    movie.watch_grade = request.POST.get('watch_grade')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')

    movie.save()

    return redirect(f'/movies/{movie_pk}')


@require_POST
def comment_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = Comment(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comments.save()
    return redirect('movies:detail', movie_pk)


@require_POST
def comment_delete(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = movie.comment_set.get(pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)