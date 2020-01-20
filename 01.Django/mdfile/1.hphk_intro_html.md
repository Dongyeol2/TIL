
# 해피해킹 과정

## 2019.10.21

#### 개발환경 설정
- 개발환경 확인
	- git bash > python -V
	Python 3.7.4
	- VS Code
- 개발환경 설정
	- VS Code 실행
	- ctrl + shift + p > default shell > git bash 선택
	- view 메뉴 > terminal 선택
- git bash cmd
	- ~ 루트에서 
```python
pip list 
python -m venv venv #가상환경 폴더생성
source ~/venv/Scripts/activate #가상환경 실행
pip list

#원하는 위치에 TIL폴더 생성
#해당폴더에서
git remote add origin https://github.com/kyunghee2/TIL.git
#파일생성
git add .
git commit -m "191021 | TIL 시작"
```
#### 웹 기초 개념
- Web Service vs Web Site
- Static Web vs Dynamic Web

#### HTML 기본
- Hyper Text Markup Language
- chrome extensions > web developer 설치해서 html, css, js 등 별도로 확인 툴
- 웹페이지 3요소
	- HTML
	- CSS
	- Javascript

#### CSS
- https://html-css-js.com/ 참고
#### 웹표준
- 팀버너스리 - W3C 월드와이드웹 창시자
- WHATWG단체 
- HTML표준안 제정
- Web Hypertext Application Technology Working Group

##### HTML 문서구조 실습
- VS Code 실행
- Tab 설정 수정 - ctrl +shift+p > setting : json 선택 > 내용추가
```json
 "[html]":{
        "editor.tabSize":2
    },
    "[css]":{
        "editor.tabSize":2
    }
```
- ctrl + / #주석생성

- html 코드작성
```html
<!-- 1. !DOCTYPE : 문서형식 선언부 -->
<!DOCTYPE html>
<!-- 2. html :문서 시작과 끝 지정-->
<!--2-1. lang : 스크린 리더, 검색 엔지 필터링 도움 -->
  <html lang="ko">
    <!-- 2.head : 브라우저에게 건네줄 정보-->
    <head>
      <meta charset="UTF-8">
      <title>인트로 페이지</title>
    </head>
    <!--실제 사용자가 볼 내용-->
    <body>
    </body>
  </html>
```

##### 검색엔진 최적화
- SEO, Search Engine Optimization 

------------
## 2019.10.22
- vs code 내에 Extensions > Live Server 모듈설치

##### HTML 기본문법
```html
  <!--글자굵게(b,strong)-->
  <p><b>굵게</b></p>
  <p><strong>굵게</strong></p>

  <!--기울림(i/em)-->
  <p><i>강조 의미를 가진 기울림</i></p>
  <p><em>강조 의미를 가진 기울림</em></p>

  <!--highlighted-->
  <p>이곳은 <mark>멀티캠퍼스 역삼</mark>입니다.</p>
  <!--취소선(del) / 밑줄(ins)-->
  <p>This is <del>del</del></p>
  <p>This is <ins>del</ins></p>

  <!--sub/sup-->
  <p>This <sub>sub</sub></p>
  <p>This <sup>sub</sup></p>

  <!--단락(p), 줄바꿈(br)-->
  <p>
    This is p!<br>
    This is p!<br>
    This is p!<br>
    This is p!<br>
  </p>

  <!--인용문 꾸미기(pre)-->
  <pre>
    from flask import flask
    app = Flask(__name__)
  </pre>
  <!--q / blockquote-->
  <q>
    창오 said, "HTML은 꿀쨈."
  </q>
  <blockquote>
    Hello, HTML!
  </blockquote>

  <!--목록(ol /ul /li)-->
  <!--순서가 있는 리스트-->
  <ol>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
  </ol>
  <ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
  </ul>

```
