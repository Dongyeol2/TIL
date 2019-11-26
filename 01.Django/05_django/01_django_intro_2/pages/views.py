from django.shortcuts import render
import requests,random

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

# 정보를 던져줄 페이지
def throw(request):
    return render(request, 'pages/throw.html')

# 사용자로부터 정보를 받아서 다시 던져줄 페이지
def catch(request):
    print(request)
    print("===")
    #=><WSGIRequest: GET '/catch/?message=sdfds'>
    print(request.GET)
    #=><QueryDict: {'message': ['sdfds']}>

    message = request.GET.get('message')
    context = {
        'message':message
    }
    return render(request, 'pages/catch.html',context)

# [실습] 아스키 아티 API를 통한 요청-응답 실습(ASCII ARTII)
# 사용자로 부터 텍스트 입력받는 페이지
def art(request):
    return render(request,'pages/art.html')

def art_result(request):    
    word = request.GET.get('word')
    
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text    
    fonts = fonts.split('\n')  

    font = random.choice(fonts)
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context ={
        'result':result
    }
    return render(request, 'pages/art_result.html',context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    user_id = request.POST.get('user_id')
    pwd = request.POST.get('pwd')
    context = {
        'user_id':user_id,
        'pwd':pwd
    }
    return render(request, 'pages/user_create.html',context)

def static_sample(request):
    return render(request, 'pages/static_sample.html')
