from django.contrib import admin
from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.index, name='index'),    # READ - Index
    #path('new/',views.new, name='new'),     # CREATE - 폼 전달
    path('create/',views.create, name='create'),   # CREATE - DB 저장
    path('<int:article_pk>/',views.detail, name='detail'),     # READ - Detail
    path('<int:article_pk>/delete', views.delete, name='delete'),     # delete
    path('<int:article_pk>/update/', views.update, name='update'),     # UPDATE - DB 저장
]
