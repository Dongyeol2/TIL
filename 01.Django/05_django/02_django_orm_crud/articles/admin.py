from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at',)
    list_display_links = ('title',) #링크설정
    list_filter = ('created_at',) #필터설정
    #list_editable = ('content',) #리스트에서 수정모드 설정
    #list_per_page = 2 #한페이지에 리스트 개수

admin.site.register(Article, ArticleAdmin)