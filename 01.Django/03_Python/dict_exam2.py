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
