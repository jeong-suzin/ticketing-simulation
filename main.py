import random
from random import choice

# 1주차
# git 계정 연결, 테스트 파일 업로드
# 좌석(이차원 list 자료구조), 경쟁자(일차원 list 자료구조) 구현

# 좌석은 3행 5열, 경쟁자는 20명으로 우선 진행
seats=[[0 for col in range(5)] for row in range(3)]
compets=[0 for col in range(20)]

# test
# seats[1][2] = -1
# print(seats)
# print(compets)


# 2주차
# 좌석별 선호도(앞줄일수록 선호도가 높도록) 난수 구현

# 선호도 난수 출력해보기
test = random.random()
print(test)

# 행에 따라 다른 선호도 난수 출력해보기 (앞 번호일수록 높은 선호도)
prefer = [15, 12, 10]
weights = []
for p in prefer:
    for r in range(5):
        weights.append(p)

seat_num = random.choices(range(0, 3*5), weights=weights) 
print(seat_num)