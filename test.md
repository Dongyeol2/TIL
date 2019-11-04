## Seed Data(Initial Data) 입력하기

```reStructuredText
우리가 애플리케이션 제작할 때 미리 준비해둔 데이터 혹은 애플리케이션 테스트용 데이터가 필요한 경우가 있다. 데이터를 하드코딩으로 일일이 넣을 수도 있다. **하지만 fixtures라는 기능을 이용해서 준비해둔 데이터를 쉽게 데이터베이스에 넣을 수 있다.**
```



## 1. 이미 데이터가 있을 경우

- ```manage.py dumpdata > movies.json``` 명령어를 통해서 현재 앱에서 가지고 있는 데이터를 빼낼 수 있다.

  ```bash
  $ python manage.py dumpdata > movies.json
  ```

  

- 이전 DB가 날아가더라도 dumpdata를 통해 빼둔 데이터들을 다시 한번 활용할 수 있다.

  

## 2. 준비해둔 fixture 데이터들을 넣고 싶은 경우

- CSV(Comma-Seperated Values)

  + 데이터들을 콤마( , )로 구분해서 비교적 간단한 텍스트 형태의 포맷으로

  + 장고에서 모델링한 

    ```
    
    ```

    

  + 프로젝트를 진행할 때 Seed Data(Initial Data)를 제공받았을 경우, Seed Data 형식을 먼저 확인하고 형식에 맞게 모델링을 진행하자!

  + Seed Data활용하는 방법

    1. 애플리케이션의 데이터베이스를 하드코딩으로 미리 만들어둔 뒤, dumpdata 명령어를 통해 fixture 데이터 형태로 만들어두고, 그 다음부턴 데이터베이스를 초기화 시켜도 loaddata명령어를 통해 다시 데이터를 불러와서 사용할 수 있다.
    2. 이미 Seed Data를 제공받았을 경우, 그냥 fixtures 폴더에 넣어두고 불러와서 사용한다.

  + fixture 데이터 내용을 바꾸거나, 모델링해둔 내용을 바꾸고 싶으면 당연히 다시 ```loaddata``` 과정을 수행한다.

    

## 3. 장고가 Fixture 파일을 찾는 방식

- 기본적으로 애플리케이션 안에 있는 ```fixtures``` 라는 디렉토리를 탐색한다.

```
movies_pjt/
	config/
	movies/
		fixtures/
			movies.json
```



- 환경설정에 ```FIXTURE_DIRS``` 옵션을 통해 장고가 바라보는 또 다른 디렉토리를 정의할 수 있다.
  + ```loaddata``` 명령어 수행할 때, 다른 경로보다 우선해서 탐색한다.

## RESTful API

```markdown
HTTP URI를 통해 자원(Resource)을 명시하고, HTTP Method(GET, POST, PUT, DELETE)를 통해 해당 자원에 대한 CRUD 로직을 적용하는 것
- 혼자 개발해서 혼자 사용할 용도면 ```articles/1/butterfly/shpw/magic```처럼 그냥 마구잡이로 개발하고 작동만 하면 된다.
- 하지만 다른 사람이 사용하는 것을 염두에 둔다면, ```[GET] articles/1```과 같이 전 세계 개발자들이 사용하는 REST아키텍처를 염두에 두고 개발해야 한다.
```

- REST 핵심 구성요소

  1. 자원(Resource) : ```URI```
  2. 행위(Verb) : ```HTTP Method```

- REST API 디자인 가이드

  + URI는 **정보의 자원**을 표현해야 한다.

  ```bash
  # URI는 자원을 표현하는데 중점을 둔다. 따라서 show, read와 같은 행위에 대한 표현이 들어가서는 안된다.
  
  GET /articles/show/1 (x)
  GET /articles/1 (o)
  ```

  

  + 자원에 대한 행위는 **HTTP Method**로 표현한다.

  ```bash
  # GET Method는 리소스 생성/삭제 등의 행위에는 어울리지 않는다.
  
  GET /articles/1/update (x)
  PUT /articles/1 (o)
  ```

  + But! Django에서는 PUT, DELETE와 같은 비공식적 요청을 default로 지원하지 않고 있기 때문에 어느정도의 절충안이 필요하다.

  ```bash
  GET /articles/2/update # 사용자에게 수정 페이지 보여줌
  POST /articles/2/update # 수정 작업 수행
  ```

##  

### 1. Modeling(```models.py```)

- possible values for ```on_delete```
  + ```CASCADE```: 부모 객체가 삭제되면 참조하는 객체도 삭제한다.
  + ```PROTECT``` : 참조가 되어 있는 경우 오류 발생
  + ```SET_NULL``` : 부모객체가 삭제되면 모든 값을 NULL로 치환 (NOT NULL 조건이면 불가능!)
  + ```SET_DEFAULT``` : 모든 값이 DEFAULT 값으로 치환(해당 값이 DEFAULT 값이 지정되어 있어야 함)
  + ```SET()``` : 특정 함수 호출
  + ```DO_NOTHING``` : 아무것도 하지 않는다. 다만, DB 필드에 대한 SQL ```on DELETE```제한 조건이 설정되어 있어야 한다.

### 2. ORM 실습

- 댓글 생성 및 조회



- 1:N Relation 활용하기
  + Article(1) : Comment(N) -> ```comment_set```
    - ```article.comment``` 형태로는 가져올 수 없다. 게시글에 몇 개의 댓글이 있는지 ```Django ORM``` 측에서 보장할 수가 없다.
  + Comment(N) : Article(1) -> ```article```
    + 댓글의 경우 ```comment.article``` 식으로 접근이 가능하다. 어떤 댓글이든 본인이 참조하고 있는 게시글은 반드시 있다. 따라서 이런 식으로 접근할 수 있다.