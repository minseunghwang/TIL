from django.shortcuts import render,redirect
from .models import Article

# Create your views here.
def index(request):
    article = Article.objects.all()[::-1]
    context = {
        'article' : article,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title)
    Article.objects.create(title=title, content=content)
    return redirect('/articles/')
    # return render(request , 'articles/create.html
    # return redirect('articles:index')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article' : article,}
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/articles/')

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article':article,}
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)