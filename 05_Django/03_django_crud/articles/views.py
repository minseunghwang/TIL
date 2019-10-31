from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()[::-1]
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# 사용자에게 게시글 작성 폼을 보여주는 함수
def new(request):
    return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    # return render(request, 'articles/create.html')
    return redirect(f'/articles/{article.pk}')

# 게시글 상세정보를 가져오는 함수
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article' : article}
    return render(request, 'articles/detail.html',context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/articles/')

# 사용자한테 게시글 수정 폼을 전달
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

# 수정 내용 전달받아서 DB에 저장(반영)
def update(request, article_pk):
    # 1. 수정할 겟글 인스턴스 가져오기 (통째로 가져오는 듯 한줄)
    article = Article.objects.get(pk=article_pk)
    # 2. 폼에서 전달받은 데이터 덮어쓰기
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 3. DB 저장 -- 내가이걸 안했누
    article.save()

    return redirect(f'/articles/{article_pk}')