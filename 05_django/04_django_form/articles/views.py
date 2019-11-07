from django.shortcuts import render, redirect, get_object_or_404
from IPython import embed
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
  articles = Article.objects.all()[::-1]
  context = {'articles':articles}
  return render(request,'articles/index.html',context)

def create(request):
  
  #사용자로부터 데이터를 받아서 DB에 저장하는 함수
  if request.method == 'POST':
    # Binding 과정
    # 폼 인스턴스를 생성하고, 전달받은 데이터를 채운다.
    # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다.
    form = ArticleForm(request.POST)
    #embed()
    if form.is_valid():
      # cleaned_data를 통해 딕셔너리 안 데이터를 검증한다.
      # title = form.cleaned_data.get('title')
      # content = form.cleaned_data.get('content')
      # article = Article.objects.create(title=title, content=content)
      article=form.save()
    return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm()

  #form으로 전달받는 형태 2가지
  # 1. GET 요청 -> 비어있는 폼 전달
  # 2. 유효성 검증 실패 -> 에러 메시지를 포함한 채로 폼 전달
  context = {'form':form}
  return render(request,'articles/form.html', context)

#게시글 상세정보를 가져오는 함수
def detail(request,article_pk):
  #article = Article.objects.get(pk=article_pk)
  article = get_object_or_404(Article, pk=article_pk)
  context = {'article':article,}
  return render(request,'articles/detail.html',context)

def delete(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  
  article.delete()
  return redirect('articles:index')
  

def update(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      article = form.save()
      return redirect('articles:detail', article.pk)
  else :
    form = ArticleForm(instance=article)
  # context로 전달되는 2가지 form 형식
  # 1. GET -> 초기값을 폼에 넣어서 사용자에게 던져줌
  # 2. POST -> is_valid로 False가 리턴됐을 때, 오류 메시지 포함해서 사용자에게 던져줌
  context = {'form':form}
  return render(request, 'articles/form.html', context)
  