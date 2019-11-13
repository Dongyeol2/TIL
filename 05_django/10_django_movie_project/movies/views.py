import csv
import hashlib
from IPython import embed
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render,redirect, get_object_or_404
from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    context ={'movies':movies,}
    return render(request,'movies/index.html',context)

@login_required
def create(request):
    # POST 요청일 경우 -> 게시글 생성 로직 수행
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            
            movie = form.save(commit = False)
            movie.user = request.user
            movie = form.save()
        return redirect('movies:detail', movie.pk)
        
    # GET 요청일 경우 -> 사용자에게 폼 보여주기
    else:
        form = MovieForm()
    context = {'form':form}
    return render(request, 'movies/form.html', context)
    
def detail(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie':movie,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request,'movies/detail.html',context)

@login_required
def update(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                movie = form.save()
            return redirect('movies:detail', movie.pk)
        else :
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:index')

    # context로 전달되는 2가지 form 형식
    # 1. GET -> 초기값을 폼에 넣어서 사용자에게 던져줌
    # 2. POST -> is_valid로 False가 리턴됐을 때, 오류 메시지 포함해서 사용자에게 던져줌
    context = {
        'form':form,
        'article':article,
    }
    return render(request, 'articles/form.html', context)

@require_POST
def delete(request,movie_pk):
    # 지금 사용자가 로그인 되어 있는가?
    if request.user.is_authenticated:
        # 삭제할 게시글 가져옴  
        movie = get_object_or_404(Movie, pk=movie_pk)
        # 지금 로그인한 사용자와 게시글 작성자 비교
        if request.user == movie.user:
            movie.delete()
        else:
            return redirect('movies:detail', movie.pk)
    return redirect('movies:index')

# 댓글 생성 뷰 함수
@require_POST
def comments_create(request, movie_pk):
    #movie = Movie.objects.get(pk=movie_pk)
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.movie_id = movie_pk
            comment.save()
        return redirect('movies:detail', movie_pk)

# 댓글 삭제 뷰 함수
@require_POST
def comments_delete(request, movie_pk, comment_pk):
    # 1. 로그인 여부 확인
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        # 2. 로그인한 사용자와 댓글 작성자가 같을 경우
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', movie_pk)
    
# def csvfilesave(request):
#     with open('data.csv', newline='', encoding='UTF8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             title = row['\ufefftitle']
#             title_en = row['title_en']
#             audience= row['audience']
#             s = row['open_date']
#             date = datetime(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))
#             open_date = date
#             genre=row['genre']
#             watch_grade=row['watch_grade']
#             score=row['score']
#             poster_url=row['poster_url']
#             description=row['description']

#             movie = Movie(title=title,title_en=title_en,audience=audience,open_date=open_date,genre=genre,watch_grade=watch_grade,score=score,poster_url=poster_url,description=description)
#             movie.save()
        
#     return render(request,'movies/save_result.html')