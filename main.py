import random
from random import choice

ROW = 3
COL = 5
COMPETS_NUM = 20

# 1주차
# git 계정 연결, 테스트 파일 업로드
# 좌석(이차원 list 자료구조), 경쟁자(일차원 list 자료구조) 구현

# 좌석은 3행 5열, 경쟁자는 20명으로 우선 진행
seats=[[0 for col in range(COL)] for row in range(ROW)]
compets=[-1 for col in range(COMPETS_NUM)]   # 0이라는 좌석번호가 있어서 -1로 수정

# test
# seats[1][2] = -1
# print(seats)
# print(compets)


# 2주차
# 좌석별 선호도(앞줄일수록 선호도가 높도록) 난수 구현

# 선호도 난수 출력해보기
test = random.random()
# print(test)

# 행에 따라 다른 선호도 난수 출력해보기 (앞 번호일수록 높은 선호도)
def select_seat_num():
    prefer = [15, 12, 10]
    weights = []
    for p in prefer:
        for c in range(COL):
            weights.append(p)
    seat_num = random.choices(range(0, COL*ROW), weights=weights) 
    # print(seat_num)
    return seat_num[0]


# 3주차
# 티켓팅 구현
# - 사용자를 제외한 모든 도전자들이 티켓팅을 시도할 좌석 번호 할당
# - 티켓팅 시도시 결제성공확률 임의 지정 후 티켓팅 결제 시도
# compets의 index 순서대로 결제시도한다고 가정
# 앞사람이 결제에 성공했어도 그 다음 사람이 결제에 성공하면 일단 티켓팅 된걸로 구현
# 
# 티켓팅 결과
# - 티켓팅 도전자들의 티켓팅 성공 여부 확인

# 사용자를 제외한 모든 도전자들이 티켓팅을 시도할 좌석 번호 할당
seat_try = [0 for col in range(COMPETS_NUM)]
for i in range(COMPETS_NUM):
    seat_try[i] = select_seat_num()
print(seat_try)

# 티켓팅 시도시 결제성공확률 임의 지정 후 티켓팅 결제 시도
def try_payment():
    result = random.choices([0, 1], weights=[7, 3])
    if result[0] == 1:
        return True
    else:
        return False

for i, s in enumerate(seat_try):
    is_success = try_payment()
    if is_success == 1:
        compets[i]=s
        r = int(s/COL)
        c = s%COL
        seats[r][c]=-1
    # else:
        # 아무것도 안함

# 티켓팅 현황 확인
print("seats ******* ")
for i in seats :
    for j in i:
        print(j, end=" ")
    print()

print("compests **** ")
print(compets)
