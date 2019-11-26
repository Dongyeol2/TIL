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

# 연습문제
# http://bit.do/yeoksam_python_33
