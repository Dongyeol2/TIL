from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)

#사용자에게 게시글 작성 폼을 보여주는 함수
def new(request):
    return render(request,'articles/new.html')

#사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    
    return redirect('articles:index')

#게시글 상세정보를 가져오는 함수
def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article
    }
    return render(request,'articles/detail.html',context)
    
# 게시글 삭제 함수
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

# 사용자에게 게시글 수정 폼을 던져주는 함수
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)

# 수정 사항을 받아서 DB에 저장(반영)하는 함수
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    #return redirect(f'/articles/{article.pk}/')
    return redirect('articles:detail',article_pk)