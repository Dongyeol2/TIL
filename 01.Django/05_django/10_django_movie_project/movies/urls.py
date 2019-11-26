from django.contrib import admin
from django.urls import path

from . import views

app_name = "movies"
urlpatterns = [
    path('', views.index,name="index"), # READ Logic - Index
    # path('new/', views.new,name="new"), 
    path('create/', views.create,name="create"), # READ Logic - Detail
    path('<int:movie_pk>/', views.detail,name="detail"), # DELETE Logic
    #path('<int:movie_pk>/edit/',views.edit,name="edit"),
    path('<int:movie_pk>/update/',views.update,name="update"), # GET(edit) / POST(update)
    path('<int:movie_pk>/delete/',views.delete,name="delete"), 
    #path('csvfilesave/',views.csvfilesave)
    path('<int:movie_pk>/comment/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/comment/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
