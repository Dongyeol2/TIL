from django.shortcuts import render, redirect
from .models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)

#사용자에게 게시글 작성 폼을 보여주는 함수
# def new(request):
#     return render(request,'articles/new.html')

#사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image=image)
        article.save()
    
        return redirect('articles:index')
    else:
        return render(request,'articles/create.html')

#게시글 상세정보를 가져오는 함수
def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    context = {
        'article':article,
        'comments':comments,
    }
    return render(request,'articles/detail.html',context)
    
# 게시글 삭제 함수
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

# 사용자에게 게시글 수정 폼을 던져주는 함수
# def edit(request, article_pk): 
#     article = Article.objects.get(pk=article_pk)
#     context = {'article': article}
#     return render(request, 'articles/edit.html', context)


# 수정 사항을 받아서 DB에 저장(반영)하는 함수
def update(request, article_pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_pk)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        #return redirect(f'/articles/{article.pk}/')
        return redirect('articles:detail',article_pk)
    else :
        article = Article.objects.get(pk=article_pk)
        context = {'article': article}
        return render(request, 'articles/update.html', context)

# 댓글 생성 뷰 함수
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment(article=article, content=content)
        comment.save()
    return redirect('articles:detail', article_pk)

# 댓글 삭제 뷰 함수
def comment_delete(request, article_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.object.get(pk=comment_pk)
        comment.delete()
    return redirect('articels:detail', article_pk)