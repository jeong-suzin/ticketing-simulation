import random
from random import choice

ROW = 3
COL = 5
COMPETS_NUM = 20

# 1주차
# git 계정 연결, 테스트 파일 업로드
# 좌석(이차원 list 자료구조), 경쟁자(일차원 list 자료구조) 구현

# 좌석은 3행 5열, 경쟁자는 20명으로 우선 진행
seat_num_user = [-1] # 사용자가 티켓팅한 좌석
seats=[[0 for col in range(COL)] for row in range(ROW)]
compets=[-1 for col in range(COMPETS_NUM)]   # 0이라는 좌석번호가 있어서 -1로 수정
prefer_value=[15,12,10]
success_p = 30

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
    if seat_num_user[0] != -1:
        seat_avail.remove(seat_num_user[0])

    prefer = []
    for a in seat_avail:
        r = int(a/COL)
        prefer.append(prefer_value[r])

    print("seat_avail", seat_avail)
    # print("prefer", prefer)
    seat_try = [0 for col in range(COMPETS_NUM)]
    for i, c in enumerate(compets):
        if c == -1: # 티켓팅 다시 할 사람
            seat_try[i] = select_seat_num(seat_avail, prefer)
        else:       # 티켓팅 이미 성공한 사람
            seat_try[i] = -1
    return seat_try

# 티켓팅 시도시 결제성공확률 임의 지정 후 티켓팅 결제 시도
def try_payment():
    result = random.choices([0, 1], weights=[100-success_p, success_p])
    if result[0] == 1:
        return True
    else:
        return False

# 티켓팅
def ticketing(seat_user, seat_try):
    print("seat try", seat_try)
    # 사용자가 제일 첫번째로 티켓팅 결제 시도
    r = int(seat_user/COL)
    c = seat_user%COL
    if seat_num_user[0] == -1 and seats[r][c] == 0:     # 티켓팅 못했는지, 시도할 좌석 팔렸는지 확인
        is_success = try_payment()  # 결제 시도
        if is_success == 1:    # 결제 성공
            seat_num_user[0]=seat_user
            seats[r][c]=-1
            print("\n결제 성공! ", seat_user,"번 좌석 겟!\n")
    # 경쟁자들
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

# 필요한 값 입력
def set_ticketing_environment():
    print ('입력값은 반드시 정수로 입력하시기 바랍니다!')
    ROW = int(input('전체 좌석의 행을 입력하세요 (ROW): '))
    COL = int(input('전체 좌석의 열을 입력하세요 (COL): '))
    COMPETS_NUM = int(input('티켓팅에 도전할 경쟁자 수를 입력하세요 (ROW X COL보다 커야 재밌습니다\'^\'): '))

    seat_num_user = [-1] # 사용자가 티켓팅한 좌석
    seats=[[0 for col in range(COL)] for row in range(ROW)]
    compets=[-1 for col in range(COMPETS_NUM)]   # 0이라는 좌석번호가 있어서 -1로 수정

    prefer_text = '앞줄 좌석 순서대로 선호도를 입력하세요 ('+ str(ROW) +'개, 각 수치는 띄어쓰기로 구분하여 입력): '
    prefer_value = list(map(int, input(prefer_text).split()))

    success_p = int(input('결제 성공 확률을 입력하세요 (0 초과 100 이하로): '))
    return ROW, COL, COMPETS_NUM, seat_num_user, seats, compets, prefer_value, success_p


################### MAIN ######################
ROW, COL, COMPETS_NUM, seat_num_user, seats, compets, prefer_value, success_p = set_ticketing_environment()

round = 1
while True:
    print("*******************", round, "번째 라운드")
    seat_try = select_seat_try()
    if seat_num_user[0] == -1:
        seat_user = int(input('티켓팅할 좌석을 입력하세요: '))
    ticketing(seat_user, seat_try)
    print_result()
    print("")

    sold_out = check_soldout()
    if sold_out:
        break
    round = round + 1


# 5주차
# - 프로그램 구현 시 이상유무 확인(testing & debugging)
# - 사용자가 라운드에 참여
# - 프로그램 구현 시 큰 이상이 없는 경우 좌석별 선호도 및 결제성공확률,
#  좌석 및 경쟁자 수 등을 입력 받아 실행할 수 있도록 프로그램 확장 시도


# 구현 후 테스트하는 과정에서 입력된 값이 예상되는 값이 아닌 경우(ex. 자료형이 다른 경우, 입력을 안한 경우)
# 프로그램이 바로 죽어버리는데 수정 및 보완하기에는 시간이 너무 오래 걸릴 것 같아 생략하였다.
# 프로그램 계획 당시에는 이러한 부분에 대해서는 미처 생각하지 못했던 사안이라
# 이후 프로젝트 진행을 하게 되는 경우 예외 처리 부분까지 고려할 수 있도록 하겠다.
