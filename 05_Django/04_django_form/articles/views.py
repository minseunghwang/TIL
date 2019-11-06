from django.shortcuts import render,redirect, get_object_or_404
from IPython import embed
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    articles = Article.objects.all()[::-1]
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    # POST 요청일 경우 -> 게시글 생성 로직 수행
    if request.method == 'POST':
        form = ArticleForm(request.POST)                # 유효성 검증
        if form.is_valid():
            article = form.save()
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)
    
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.method == 'POST':
        article.delete()
        return redirect('/articles/')
    else:
        return redirect('articles:detail', article.pk)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = { 'form' : form }
    return render(request, 'articles/form.html', context)