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



