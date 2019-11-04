from django.shortcuts import render,redirect
from .models import Movie
import csv
from datetime import datetime

# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    context ={
        'movies':movies
    }
    print(movies)
    return render(request,'movies/index.html',context)

# def new(request):
#     return render(request,'movies/new.html')

def create(request):
    # POST 요청일 경우 -> 게시글 생성 로직 수행
    if request.method == 'POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        movie = Movie(title=title,title_en=title_en,audience=audience,open_date=open_date,genre=genre,watch_grade=watch_grade,score=score,poster_url=poster_url,description=description)
        movie.save()
        return redirect('movies:index')
        
    # GET 요청일 경우 -> 사용자에게 폼 보여주기
    else:
        return render(request,'movies/create.html')

    

# def edit(request,movie_pk):
#     movie = Movie.objects.get(pk=movie_pk)
#     context = {'movie': movie}
#     return render(request,'movies/edit.html',context)

def update(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk) # 중복되니깐 밖으로 뺌

    # POST 요청 -> DB에 수정사항 반영
    if request.method == 'POST':
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
        return redirect('movies:detail',movie_pk)

    # GET 요청 -> 사용자에게 수정 Form 전달
    else:
        context = {'movie': movie}
        return render(request,'movies/update.html',context)

def detail(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie':movie
    }
    return render(request,'movies/detail.html',context)
    
def delete(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()

    return redirect('movies:index')

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