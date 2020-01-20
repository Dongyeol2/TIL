from django.contrib import admin
from .models import Movie, Comment

# Register your models here.
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk','title','title_en','audience','open_date','genre','watch_grade','score','poster_url','description')
    list_display_links = ('title',) #링크설정
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)