# 19.11.07 Django Form 마무리

## 1. URL Resolver

- CREATE 로직과 UPDATE 로직이 같은 템플릿(form.html)을 공유하고 있는데, 둘 다 ```<h1>CREATE<h1>```라는 헤더가 출력되고 있다.

- URL Resolver는 사용자가 요청한 URL과 장고 내부로 들어오는 URL 사이에서 번역 역할을 해준다.

  

## 2. Django Bootstrap



## 3. Comment-ModelForm

- Comment Model 생성
- Comment ModelForm 생성
- admin.py 등록

## 4. View Decorators

```
Django가 제공하는 decorator 활용하기
```

### 4.1 require_POST

- view 함수가 POST 메서드 요청만 승인하도록 하는 데코레이터
- 일치하지 않는 요청이면 405 Method Not Allowed 에러 발생시킴

## Authentication(인증)

```markdown
장고에서 이미 Auth관련 기증을 만들어두었고, 우리ㅡㄴ 자연스럽게 사용하고 있었다. ```createsuperuser```를 통해 계정도 만들었고, Admin 페이지에서 로그인 기능도 사용하고 있었다.
```

### 1. Accounts

- 기존 앱에서 구현해도 되지만, 장고에서 기능 단위로 애플리케이션을 나누는 것이 일반적이므로 ```accounts```라는 새로운 앱을 만들어보자.

- accounts 앱 생성

  ```bash
  $ python manage.py startapp accounts
  ```

  ```bash
  # settings.py
  
  INSTALLED_APPS = [
  	'articles',
  	'accounts',
  	...
  ]
  ```

- URL 분리

  ```python
  # config/urls.py
  
  # accounts/urls.py
  ```

### 2. Sine Up

