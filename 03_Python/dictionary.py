# 1. 딕셔너리 만들기(2가지)
lunch = {
    '중국집' : '032'
}
lunch = dict(중국집 = '032')

# 2.딕셔너리 추가하기
lunch['분식집'] = '031'

# 3. 딕셔너리 내용 가져오기 (2가지)
artists = {
    '아티스트' : {
        '민수' : '민수는 혼란스럽다',
        '아이유' : '좋은날'
    }
}
# 민수의 대표곡은 ?
# print(artists['아티스트']['민수'])
# print(artists.get('아티스트').get('아이유'))


# 1.4 딕셔너리 반복문 활용하기 
# 1.4.1 기본 활용
print(lunch) 
for key in lunch:
    print(key)              # key 출력됨
    print(lunch[key])       # key로 value 추출


# 1.4.2 Key, Value 모두 가져오기
for key,value in lunch.items():
    print(key,value)



print("뀨우?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# 1.4.3 Value만 가져오기
for value in lunch.items():
    print(value)
    #=> 중국집, 분식집
 


# 1.4.4 key만 가져오기
for value in lunch.items():
    print(key)






print("가즈악@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")



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
sum = 0
for key in score:
    sum += int(score[key])
print(sum/len(score))

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
totalsum = 0
for key in scores:
    sum = 0
    new_score = scores[key]
    for key2 in new_score:
        sum += int(new_score[key2])
    totalsum += int(sum/len(new_score))
print(totalsum/len(scores))




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

for key,value in cities.items():
    sum = 0
    for i in value:
        sum += int(i)
    print(key,":",int(sum/3))


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

cold = 0
hot = 0
count = 0
hot_city = ""
cold_city = ""

for name, temp in cities.items():
    # 첫 번째 시행
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0: # 첫번째 시행을 위한 처리 
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가 cold보다 더 추우면, cold에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        # 최고 온도가 hot보다 더 더우면, hot에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1

print(hot_city)
print(cold_city)






# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

print(2 in cities['서울'])