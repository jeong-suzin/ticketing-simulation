# ticketing-simulation
1.목표
- 실생활에서 접할 수 있는 티켓팅 프로세스에 대한 프로그램화를 목적으로, 좌석선택 및 결제를 한 라운드로 하여 티켓이 매진되면 종료되는 프로그램을 설계한다.

2. 주차별 진행(예정)내용
- 1주차
    - git 계정 연결, 테스트 파일 업로드 등을 통해 개발 환경 점검
    - 좌석(이차원 list 자료구조), 경쟁자(일차원 list 자료구조) 구현

- 2주차
    - 좌석별 선호도(앞줄일수록 선호도가 높도록) 난수 구현

- 3주차
    - 결제성공확률 임의 지정 및 최종 티켓팅 성공 여부 확인
    (먼저 좌석을 선택한 한 사람만 결제시도 가능, 후선택자는 고려하지 않음)

- 4주차
    - Queue를 통해 동일좌석 선택자에 대한 결제시도 순서 부여

- 5주차
    - 프로그램 구현 시 이상유무 확인(testing & debugging)
    - 프로그램 구현 시 큰 이상이 없는 경우 좌석별 선호도 및 결제성공확률, 좌석 및 경쟁자 수 등을 입력 받아 실행할 수 있도록 프로그램 확장 시도
