# 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
# 키보드로부터 0~9 사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)
# 아래 경우 게임 Lose
#   - 시도 횟수 >= 5
#   - Strike out == 2
# 아래 경우 세이 Win
#   - 컴퓨터에서 생성 한 난수 값을 자리 순서대로 맞출 경우
# 출력 포맷은 아래와 동일 할 것
#   - 출력 내용에 시도 횟수 카운트,
#       아웃 횟수 카운트, Strike Ball 판별 결과, 게임 결과, 정답 포함
#---------------------------------------------------------------------
import random
import os
# 0~9사이의 3개 정수를 random.randint() API를 이용하여 난수로 생성.
random_things = []
subrandom = 0
for randomint in range(3): # 3번 돌리기
    subrandom = random.randint(0, 9)
    while True: # 지속반복 하며 중복 확인
        if subrandom not in random_things: # 중복값이 없을 시 저장 후 확인 탈출
            random_things.append(subrandom)
            break
        else: # 중복값이 있을 시 다시돌림
            subrandom = random.randint(0, 9)
            
# print(random_things) # 임시 확인용
#---------------------------------------------------------------------
# 전체적인 게임 반복문
flag = True
out_value = 0 # 아웃 횟수
try_value = 0 # 시도 횟수
strike = 0
ball = 0
while flag:
    try_value += 1 # 시도 횟수 증가
    
    # 승패 조건문
    # Lose 조건문
    if (try_value >= 5 or out_value == 2) and strike != 3:
        if try_value >= 5:
            print("게임횟수 초과")
        elif out_value == 2:
            print("아웃횟수 초과")
        print("아까비~~~졌네용..")
        print("정답은:", random_things, "입니다.")
        break
    # Win 조건문
    elif strike == 3:
        print("Win")
        break
    
    # 카운트 초기화
    strike = 0
    ball = 0
    # 시도횟수 출력
    if try_value < 5:
        print("시도횟수:", try_value)
    
    # 키보드로부터 0~9 사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)
    input_list = [] # 입력값 리스트 저장용
    input_value = input("정수 3개를 입력하세용~~^__^\n") # 값 입력받기
    for value in input_value: # 입력 값의 수만큼 반복
        input_list.append(int(value)) # 현재 값 순서대로 저장

    # print(input_list) # 임시 확인용
    #---------------------------------------------------------------------
    # 판독
    for list_num in range(3):
        # 자리, 값 모두 맞을 시 Strike 추가
        if random_things[list_num] == input_list[list_num]:
            strike += 1
        # 값 만 맞을 시 Ball 추가
        elif input_list[list_num] in random_things:
            ball += 1
            
    print("") # 줄 정리
    # strike와 ball 모두 없을 시 out 출력
    if strike == 0 and ball == 0:
        print("Out")
        out_value += 1 # 아웃 횟수 증가
    # 그 외 통상출력
    else:
        print(strike, "Strike", ball, "Ball")
    print("") # 줄 정리
    
    #---------------------------------------------------------------------

# 계속하려면 아무 키나 누르십시오 . . .
os.system("pause")