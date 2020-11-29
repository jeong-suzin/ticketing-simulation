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

# 행에 따라 다른 선호도 난수 출력해보기 (앞 번호일수록 높은 선호도)
def select_seat_num(seat_avail, prefer):
    # prefer = [15, 12, 10]
    # weights = []
    # for p in prefer:
    #     for c in range(COL):
    #         weights.append(p)
    seat_num = random.choices(seat_avail, weights=prefer) 
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
def select_seat_try():
    # 안 팔린 좌석만
    seat_avail = list(range(0, COL*ROW))
    for c in compets:
        if c != -1:
            seat_avail.remove(c)

    prefer = []
    for a in seat_avail:
        if 0 <= a < COL:
            prefer.append(15)
        elif COL <= a < COL*2:
            prefer.append(12)
        elif COL*2 <= a < COL*3:
            prefer.append(10)

    print("seat_avail", seat_avail)
    print("prefer", prefer)
    seat_try = [0 for col in range(COMPETS_NUM)]
    for i, c in enumerate(compets):
        if c == -1: # 티켓팅 다시 할 사람
            seat_try[i] = select_seat_num(seat_avail, prefer)
        else:       # 티켓팅 이미 성공한 사람
            seat_try[i] = -1
    return seat_try

# 티켓팅 시도시 결제성공확률 임의 지정 후 티켓팅 결제 시도
def try_payment():
    result = random.choices([0, 1], weights=[7, 3])
    if result[0] == 1:
        return True
    else:
        return False

# 티켓팅
def ticketing(seat_try):
    print("seat try", seat_try)
    for i, s in enumerate(seat_try):
        r = int(s/COL)
        c = s%COL
        if compets[i] == -1 and seats[r][c] == 0:     # 티켓팅 못했는지, 시도할 좌석 팔렸는지 확인
            is_success = try_payment()  # 결제 시도
            if is_success == 1:    # 결제 성공
                compets[i]=s
                seats[r][c]=-1
            # else:
                # 아무것도 안함

# 티켓팅 현황 확인
def print_result():
    print("seats ******* ")
    for i in seats :
        for j in i:
            print(j, end=" ")
        print()

    print("compests **** ")
    print(compets)

# 4주차
# 티켓팅은 compets 순서대로 진행됨 --> 동일 좌석에 대해 이미 팔렸다면 티켓팅 시도 불가
# 좌석이 매진될 때까지 라운드로 구현
# - 이미 티켓팅한 사람은 다음 라운드에서 도전 안함
# - 다음 라운드에서 티켓팅 재도전 하는 사람들이 티켓팅할 좌석을 고를 때 이미 팔린 좌석은 선택 안함
def check_soldout():
    sold_out = False
    for seat_row in seats:
        if 0 in seat_row:
            sold_out = False
            break
        else:
            sold_out = True
    print(sold_out)
    print("")
    return sold_out

round = 1
while True:
    print(round, "번째 라운드")
    seat_try = select_seat_try()
    ticketing(seat_try)
    print_result()
    print("")

    sold_out = check_soldout()
    if sold_out:
        break
    round = round + 1