
#### CSS 
- vs code tip
```
ctrl+alt: 여러 요소 한번에 수정
shift + alt + 화살표 아래 : 커서 위치에 동일한 요소 추가
```
- css 참고 사이트
	- https://www.youtube.com/watch?v=ea69CKqsVMg
	- 
##### CSS 기본문법
- 선택자 {속성:값}
	- 선택자(Selector): h1
	- 선언블록:{...}

##### CSS 실습

- 무료 이미지 unsplash
- Position
	- static : 기본위치
	- relative: 상대위치
	- absolute: 절대위치
		- 부모요소 또는 조상개체 속성에 따라 영향이 미침
		- 조상 개체중에 relative가 있으면 해당 개체를 기준으로 이동

##### CSS 심화 실습
- http://bit.do/yeoksam_position 과제
- box2.html 추가
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>BOX</title>
  <link rel="stylesheet" href="box2.css">
</head>
<body>
  <div class="big-box">
    <div class="small-box" id="red"></div>
    <div class="small-box" id="gold"></div>
    <div class="small-box" id="green"></div>
    <div class="small-box" id="blue"></div>
    <div class="small-box" id="pink"></div>
    
    <div class="small-box" id="green">
      <div class="small-box" id="purple"></div>
    </div>
    <div class="small-box" id="blue">
      <div class="small-box" id="orange"></div>
    </div>
  </div>
</body>
</html>
````
- box2.css 추가
```css
.big-box {
  position: relative;
  margin: 100px auto 500px;
  border: 5px solid black;
  width: 500px;
  height: 500px;
}

.small-box {
  width: 100px;
  height: 100px;
}

#red {
  background-color: red;
  /* 큰 사각형 내부의 우측 하단 모서리에 빨간 사각형 위치시키기 */
  position: absolute;
  bottom: 0px;
  right: 0px; 
}

#gold_back {
  background-color: gold;
  /* 브라우저의 하단에서 50px, 우측에서 50px 위치에 고정하기 */
  position: absolute;
  bottom: -300px;
  right: -300px;
}
#gold {
  background-color: gold;
  /* 브라우저의 하단에서 50px, 우측에서 50px 위치에 고정하기 */
  position: fixed;
  bottom: 50px;
  right: 50px;
}

#green {
  background-color: green;
  /* absolute 이용해서 큰 사각형의 가운데 위치시키기 */
  position: absolute;
  top: 200px;
  left: 200px;
}

#blue {
  background-color: blue;
  /* relative를 사용해서 큰 사각형 좌측 상단 모서리에서 100px, 100px 띄우기 */
  position: absolute;
  top: 100px;
  left: 100px;
}

#pink {
  background-color: pink;
  /* 큰 사각형 내부의 좌측 상단 모서리로 옮기기*/
  position: absolute;
  top: 0px;
  left: 0px;
}

#purple {
  background-color: purple;
  /* 초록 사각형의 우측 하단 모서리에 보라 사각형 좌측 상단 모서리 맞대기 */
  position: absolute;
  top: 100px;
  left: 100px;
}

#orange {
  background-color: orange;
  /* 파란 사각형 오른쪽 위 모서리에 오렌지 사각형 좌측 하단 모서리 맞대기 */
  position: absolute;
  top: -100px;
  left: 100px;
}

```

![div1](https://user-images.githubusercontent.com/33045725/67268955-b3f4bd00-f4f0-11e9-9207-9db0d5b0d6da.JPG)


##### 기타
- https://stackshare.io/ : 기술 동향 확인 사이트 
- https://github.com/devJang/developer-roadmap/blob/master/readme.md 개발자 로드맵
