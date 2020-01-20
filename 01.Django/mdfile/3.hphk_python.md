2019.10.23

# Python
## Python Dictionary
### 1. 기본기
- 가장 많이 사용되는 자료형 + 웹 개발하면서 마주칠 가능성이 가장 높음
- 딕셔너리는 기본적으로 key 와 value 구조
	- key: string, integer, float, boolean가능 
	- value: 모든 자료형 가능, list, dictionary 가능
```python
# 1. 딕셔너리 만들기
lunch = {
    '중국집':'032'
}
lunch = dict(중국집='032')

# 2. 딕셔너리 내용 추가하기
lunch['분식집'] = '031'

# 3. 딕셔너리 내용 가져오기
artists = {
    '아티스트':{
        '민수':'민수는 혼란',
        '아이유':'좋은날'
    }
}
# 민수의 대표곡은?
print(artists["아티스트"]["민수"])
print(artists.get("아티스트").get("민수"))

# 1.4 딕셔너리 반복문 활용하기
# 1.4.1 기본활용
for key in lunch:
    print(key)
    print(lunch[key])

# 1.4.2 .items : key, value 모두 가져오기
for key, value in lunch.items():
    print(key, value)

# 1.4.3 .values : value만 가져오기
for value in lunch.values():
    print(value)

# 1.4.4 .keys : key만 가져오기
for key in lunch.keys():
    print(key)
```

### 2. 연습문제
```python
# 연습문제
# http://bit.do/yeoksam_python_33

# 강사님 코드 : bit.do/yeoksam_answer
'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
score_sum=0
for x in score.values():
    score_sum += x
score_avg = score_sum /len(score)

print(f'평균은? {score_avg}')

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    '민승': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    '건희': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
score_sum=0
score_avg=0
#total =0
for x in scores.values():
    score_sum=0
    for y in x.values():        
        score_sum += y
    
    score_avg += score_sum / len(x)
    #score_avg += total

print(f'전체평균은? {score_avg/len(scores)}')


# 3. 도시별 최근 3일의 온도입니다.
cities = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
'''
출력 예시)
서울 : 평균온도
대전 : 평균온도
광주 : 평균온도
부산 : 평균온도
'''
temp_sum=0
for city,temp in cities.items():
    temp_sum=0
    for x in temp:
        temp_sum += x
        #print(x)
    print(f'{city}: {temp_sum/len(temp)}')

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
t_min =0
t_max =0
t_min_nm=''
t_max_nm=''
for city,temp in cities.items():
    for x in temp:
        if x < t_min:
            t_min = x
            t_min_nm = city
        elif x > t_max:
            t_max = x
            t_max_nm = city
           
print(f'가장 추웠던 곳:{t_min_nm}, 가장 더웠던 곳:{t_max_nm}')

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in cities["서울"]:
    print("있어요")
else:
    print("없어요!")

```

### 3. 실습문제

```python
t4ir = {
    "location": ["역삼", "강남", "삼성", "왕십리"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scraping": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "connected":  {
            "lecturer": "유창오",
            "manager": "유주희",
            "class president": "정세환",
            "groups": {
                "A": ["정세환", "오은애", "황민승", "소현우", "김한석"],
                "B": ["최재범", "서혁진", "감자", "이도현", "합기도"],
                "C": ["이수연", "남찬우", "이승희", "은승찬", "김건"],
                "D": ["박경희", "김영선", "이동열", "이건희", "최찬종"],
                "E": ["공선아", "최주현"]
            }
        },
        "bigdata": {
            "lecturer": "이민교",
            "manager": "매니저"
        }
    }
}


'''
난이도* 1. 지역(location)은 몇개 있나요? : list length
출력예시)
4
'''
print('==== Q1 ====')
print(len(t4ir["location"]))
print(len(t4ir.get('location')))



'''
난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
출력예시)
False
'''
print('==== Q2 ====')
print('requests' in t4ir['language']['python']['python standard library'])
print('requests' in t4ir.get('language').get('python').get('python standard library'))


'''
난이도** 3. connected반의 반장의 이름을 출력하세요. : depth 있는 접근
출력예시)
정세환
'''
print('==== Q3 ====')
print(t4ir['classes']['connected']['class president'])
print(t4ir.get('classes').get('connected').get('class president'))


'''
난이도*** 4. t4ir에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
출력 예시)
python
web
'''
print('==== Q4 ====')
for lang in t4ir['language'].keys():
    print(lang)

# 혹은
for name in t4ir.get('language'):
    print(name)

# 딕셔너리에서 for문 돌리면 key 값이 나옴
for name in t4ir:
    print(name)
'''
location 
language
classes
'''




'''
난이도*** 5 t4ir bigdata반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
출력 예시)
이민교
매니저
'''
print('==== Q5 ====')
for name in t4ir['classes']['bigdata'].values():
    print(name)

for name in t4ir.get('classes').get('bigdata').values():
    print(name)


'''
난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
'''
print('==== Q6 ====')
# 방법 1
frameworks = t4ir['language']['python']['frameworks']
for name in frameworks:
    print(f'{name}은 {frameworks[name]}이다.')

# .get
frameworks = t4ir.get('language').get('python').get('frameworks')
for name in frameworks:
    print(f'{name}은 {frameworks[name]}이다.')



# 방법 2
for name, attr in t4ir['language']['python']['frameworks'].items():
    print('{}는 {}이다.'.format(name, attr))

# .get
for name, attr in t4ir.get('language').get('python').get('frameworks').items():
    print(f'{name}은(는) {attr}이다.')



'''
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 E 그룹에서 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
출력예시)
오늘의 당번은 황민승
'''
print('==== Q7 ====')
import random

lucky = random.choice(t4ir.get('classes').get('connected').get('groups').get('A'))
print(f'오늘의 당번은 {lucky}님.')

```


