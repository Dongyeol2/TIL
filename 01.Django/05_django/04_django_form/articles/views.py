import hashlib
from itertools import chain
from IPython import embed
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
  # if request.user.is_authenticated:
  #   gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()
  # else:
  #   gravatar_url = None

  articles = Article.objects.all()
  context = {'articles':articles,}
  return render(request,'articles/index.html',context)

@login_required
def create(request):
  #사용자로부터 데이터를 받아서 DB에 저장하는 함수
  if request.method == 'POST':
    # Binding 과정
    # 폼 인스턴스를 생성하고, 전달받은 데이터를 채운다.
    # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다.
    form = ArticleForm(request.POST)
    # embed()
    if form.is_valid():
      # cleaned_data를 통해 딕셔너리 안 데이터를 검증한다.
      # title = form.cleaned_data.get('title')
      # content = form.cleaned_data.get('content')
      # article = Article.objects.create(title=title, content=content)
      article = form.save(commit = False)
      article.user = request.user
      article=form.save()
      # hashtag
      # 게시글 내용을 split해서 리스트로 만듦
      for word in article.content.split():
        # word가 '#'으로 시작할 경우 해시태그 등록
        if word.startswith('#'):
          hashtag, created = Hashtag.objects.get_or_create(content=word)
          article.hashtags.add(hashtag)
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
  
  person = get_object_or_404(get_user_model(), pk=article.user_id)
  comment_form = CommentForm()
  comments = article.comment_set.all()
  context = {
    'article':article,
    'person':person,
    'comment_form':comment_form,
    'comments':comments,
  }
  return render(request,'articles/detail.html',context)

@require_POST
def delete(request, article_pk):
  # 지금 사용자가 로그인 되어 있는가?
  if request.user.is_authenticated:
    # 삭제할 게시글 가져옴  
    article = get_object_or_404(Article, pk=article_pk)
    # 지금 로그인한 사용자와 게시글 작성자 비교
    if request.user == article.user:
      article.delete()
    else:
      return redirect('articles:detail', article.pk)
  return redirect('articles:index')
  
@login_required
def update(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  if request.user == article.user:
    if request.method == 'POST':
      form = ArticleForm(request.POST, instance=article)
      if form.is_valid():
        article = form.save()
        # hashtag
        article.hashtags.clear()
        for word in article.content.split():
          if word.startswith('#'):
            hashtag, create = Hashtag.objects.get_or_create(content=word)
            article.hashtags.add(hashtag)

        return redirect('articles:detail', article.pk)
    else :
      form = ArticleForm(instance=article)
  else:
    return redirect('articles:index')

  # context로 전달되는 2가지 form 형식
  # 1. GET -> 초기값을 폼에 넣어서 사용자에게 던져줌
  # 2. POST -> is_valid로 False가 리턴됐을 때, 오류 메시지 포함해서 사용자에게 던져줌
  context = {
    'form':form,
    'article':article,
  }
  return render(request, 'articles/form.html', context)

# 댓글 생성 뷰 함수
@require_POST
def comment_create(request, article_pk):
  # article = get_object_or_404(Article, pk=article_pk)
  if request.user.is_authenticated:
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      # save 메서드 -> 선택 인자 : (기본값) commit=True
      # commit=False : DB에 바로 저장되는 것을 막아준다.
      comment = comment_form.save(commit=False)
      comment.user = request.user
      comment.article_id = article_pk
      comment.save()
  return redirect('articles:detail', article_pk)


#댓글 삭제 뷰 함수
@require_POST
def comment_delete(request, article_pk, comment_pk):
  # 1. 로그인 여부 확인
  if request.user.is_authenticated:
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 2. 로그인한 사용자와 댓글 작성자가 같을 경우
    if request.user == comment.user:
      comment.delete()
  return redirect('articles:detail', article_pk)

@login_required
def like(request, article_pk):
  # 좋아요 누를 게시글 가져오기
  article = get_object_or_404(Article, pk=article_pk)
  # 현재 접속하고 있는 유저
  user = request.user

  # 현재 게시글을 좋아요 누른 사람 목록에서, 
  # 현재 접속한 유저가 있을 경우 -> 좋아요 취소
  if user in article.like_users.all():
    article.like_users.remove(user)
  # 목록에 없을 경우 -> 좋아요 누르기
  else:
    article.like_users.add(user)
  return redirect('articles:index')

@login_required
def follow(request, article_pk, user_pk):
  # 게시글 작성한 유저
  person = get_object_or_404(get_user_model(), pk=user_pk)
  # 지금 접속하고 있는 유저
  user = request.user
  # 게시글 작성 유저 팔로워 명단에 접속 중인 유저가 있을 경우
  # -> 언팔
  if person != user :
    if user in person.followers.all():
      person.followers.remove(user)
    # 명단에 없으면
    # -> 팔로우
    else:
      person.followers.add(user)
    # 게시글 상세정보로 redirect
  return redirect('articles:detail', article_pk)

# 내가 팔로우 하는 사람의 글 + 내가 작성한 글
def list(request):
  # 내가 팔로우하고 있는 사람들
  followings = request.user.followers.all()
  # 내가 팔로우하고 있는 사람들 + 나 -> 합치기
  followings = chain(followings, [request.user])
  # 위 명단 사람들 게시글 가져오기
  articles = Article.objects.filter(user__in=followings).order_by('-pk').all()
  comment_form = CommentForm()
  context = {
    'articles':articles,
    'comment_form':comment_form,
  }
  return render(request, 'articles/article_list.html', context)

# 모든 사람 글
def explore(request):
  articles = Article.objects.all()
  comment_form = CommentForm()
  context = {
    'articles':articles,
    'comment_form':comment_form,
  }
  return render(request, 'articles/article_list.html', context)

def hashtag(request, hash_pk):
  # 해시태그 가져오기
  hashtag = get_object_or_404(Hashtag, pk=hash_pk)
  # 해당 해시태그를 참조하는 게시글들 가져오기
  articles = hashtag.article_set.order_by('-pk')
  context = {
    'hashtag' : hashtag,
    'articles' : articles,
  }
  return render(request, 'articles/hashtag.html', context)