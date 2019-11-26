from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm) :
  title = forms.CharField(
    label='제목',
    max_length=10,
    widget=forms.TextInput(
      attrs={
        'class':'title',
        'placeholder':'제목 입력해라...',
      }
    )
  )
  title_en = forms.CharField(
    label='영어 제목',
    max_length=10,
    widget=forms.TextInput(
      attrs={
        'class':'title_en',
        'placeholder':'영어제목 입력해라...',
      }
    )
  )
  audience = forms.IntegerField(
    label='관객',
    widget=forms.TextInput(
      attrs={
        'class':'audience',
      }
    )
  )
  open_date = forms.DateTimeField(
    label='날짜',
    widget=forms.TextInput(
      attrs={
        'class':'open_date',
      }
    )
  )
  genre = forms.CharField(
    label='장르',
    max_length=10,
    widget=forms.TextInput(
      attrs={
        'class':'genre',
      }
    )
  )
  watch_grade = forms.CharField(
    label='본사람',
    max_length=10,
    widget=forms.TextInput(
      attrs={
        'class':'watch_grade',
      }
    )
  )
  score = forms.FloatField(
    label='평점',
    widget=forms.TextInput(
      attrs={
        'class':'score',
      }
    )
  )
  poster_url = forms.CharField(
    label='포스터',
    max_length=10,
    widget=forms.TextInput(
      attrs={
        'class':'poster_url',
      }
    )
  )
  description = forms.CharField(
    label='내용',
    widget=forms.Textarea(
      attrs={
        'class':'description',
        'placeholder':'내용 입력해라...',
        'rows':5,
        'cols':30,
      }
    )
  )

  # 메타 데이터 -> 데이터의 데이터
  # ex) 사진 한장 (촬영장비 이름, 촬영환경 등)
  class Meta:
    model = Movie
    fields = ('__all__')

class CommentForm(forms.ModelForm):
  content = forms.CharField(
    label='댓글',
    widget=forms.Textarea(
      attrs={
        'class':'content',
        'placeholder':'댓글 입력해라...',
        'rows':1,
        
      }
    )
  )

  class Meta:
    model = Comment
    fields = ('content',)

