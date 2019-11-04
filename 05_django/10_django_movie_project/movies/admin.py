from django.contrib import admin

# Register your models here.
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk','title','title_en','audience','open_date','genre','watch_grade','score','poster_url','description')
    list_display_links = ('title',) #링크설정
    

admin.site.register(Movie, MovieAdmin)