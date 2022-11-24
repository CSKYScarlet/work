import random

# 변수들 ------------------------------
random_list = [] # 리스트
list_sum = 0 # 합계
list_min = 99 # 최소
list_max = 0 # 최대
list_trauma = [] # 중복 값
trauma_value = [] # 중복 하는 값의 중복 횟수를 저장
count = 0 # 횟수 저장용 변수
count_list = [0, 0, 0, 0] # 구간별로 카운트값 저장
#---------------------------------------------------------
print("랜덤 값 :", end="")

# 1~20 사이 양의 정수 중 난수 값 20개 생성 수 List에 저장
for repeat in range(20):
    random_list.append(random.randint(1, 20))
    if repeat % 10 == 0:
        print("\n\t", end="")
    print(" ", random_list[repeat], end="")
    # 줄 꾸밈용
    if random_list[repeat] < 10:
        print(" ", end="")
    
    list_sum += random_list[repeat]
    
    # 최소 갱신
    if random_list[repeat] <= list_min:
        list_min = random_list[repeat]
    # 최대 갱신
    elif random_list[repeat] >= list_max:
        list_max = random_list[repeat]
print("")
#---------------------------------------------

# 리스트값 세이브
subrandom_list = random_list.copy()

# List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 출력
print("최소 값 :", list_min)
print("최대 값 :", list_max)
print("합계 \t:", list_sum)
print("평균 \t:", list_sum / 20)

# 중복--------------------------------------
# List 내 중복 값과 중복 횟수 정보 출력
# 중복 값 계산
for value in random_list:
    for subvalue in random_list:
        if value == subvalue:
            count += 1
            
    if count > 1:
        list_trauma.append(value)
        trauma_value.append(count)
        for count_value in range(count):
            random_list.remove(value)
    count = 0
        
# 헤더 텍스트 출력
print("중복 값\t  중복 회수")
# 중복되는 값의 수 만큼 반복 후 해당 수와 반복횟수 출력
for value in list_trauma:
    print(" ", value, "\t   ", trauma_value[count])
    count += 1
    
count = 0 # 카운트 초기화

# 히스토그램--------------------------------
# 구간별 히스토그램 정보 출력
# 구간별 히스토그램 값 누적
#헤더 텍스트 출력
print("구간별 히스토그램")

for value in subrandom_list:
    if value < 6 and value > 0:
        count_list[0] += 1
        
    elif value < 11 and value > 5:
        count_list[1] += 1
        
    elif value < 16 and value > 10:
        count_list[2] += 1
        
    elif value < 21 and value > 15:
        count_list[3] += 1
        
# 히스토그램 출력
for history in count_list:
    if count == 0:
        print(" 1 ~  5 : ", end="")
    elif count == 1:
        print(" 6 ~ 10 : ", end="")
    elif count == 2:
        print("11 ~ 15 : ", end="")
    elif count == 3:
        print("16 ~ 20 : ", end="")
        
    for subhistory in range(history):
        print("*", end="")
        
    print("")
    count += 1