# 1주차
# git 계정 연결, 테스트 파일 업로드
# 좌석(이차원 list 자료구조), 경쟁자(일차원 list 자료구조) 구현

# 좌석은 3행 5열, 경쟁자는 20명으로 우선 진행
seats=[[0 for col in range(5)] for row in range(3)]
compets=[0 for col in range(20)]

# test
seats[1][2] = -1
print(seats)
print(compets)