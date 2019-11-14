# 2019.11.14 Hashtag / Social Login

## 1. Hashtag

### 1.1 Model

- `unique=True`
  + True인 경우, 필드는 테이블을 전체에서 고유한 값이어야 한다.
  + 유효성 검사 단계에서 실행되며, 중복 값이 있는 모델을 저장하려고 하면 `.save()`메서드로 인해서 에러가 발생한다.

1. 사용자가 업로드한 content

2. `.split()`메소드로 단어 구분

3. 리스트 반복문 돌리기 : 앞자리가 '#'으로 시작하는 단어를 해시태그 등록 - 같은 태그가 오면 unique=True 옵션으로 인해 에러 발생. 이를 방지하기 위해 `get_or_create()` 사용
4. 

### 1.2 View & URL

### 1.3 CREATE

### 1.4 UPDATE

### 1.5 READ

## 2. Social Login

인증, 계정, 등록 등을 다루는 여러가지 방법이 존재하는데,  우리는 `django-allauth`라는 **라이브러리를 사용해서 손쉽게 Social Login을 구현해 보자.**

대부분의 소셜 로그인을 지원하고 회원가입 시킬 수 있다.

### 2.1 사전 준비



### 2.2 Kakao Developers OAuth 등록