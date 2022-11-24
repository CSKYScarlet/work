# 1. 1~50 사이의 중복되지 않은 정수형 난수 25개를 선택하여 LIST에 저장
# 2. 각 열, 행 별 최대, 최소, 중간 값을 찾아 출력하라.
#  - 중간 값: 데이터들을 크기순으로 배열 했을 때 전체의 중앙에 위치하는 수
#  예) 1, 3, 5, 10, 4 -> 중간 값: 4
# 4. LIST 전체를 기준으로 최대, 최소, 중간 값을 출력하라.

# random import
import random

# 1~50 사이의 정수형 난수 25개 생성하여 LIST에 저장
random_list = []
save_random = 0
for value in range(25): # 25개의 난수 생성
    save_random = random.randint(1, 50)
    # 중복될 경우 비중복 시 까지 재생성
    # while
    while True:
        if save_random in random_list:
            save_random = random.randint(1, 50)
        else: # LIST 내부에 존재하지 않을 시 저장 후 검수 종료
            random_list.append(save_random)
            break
    
# print(random_list)
# LIST 내의 정수를 정렬
sort_list = random_list.copy()
sort_list.sort()
# print(sort_list)
# 정렬 출력
for value in range(len(random_list)):
    # 줄꾸밈
    if value % 5 == 0 and value != 0:
        print("|")
        
    # 현제 정수 출력
    print("|", random_list[value], end=" ")
    if random_list[value] < 10: # 한자리 수 줄맞춤
        print(" ", end="")
        
    # 줄꾸밈
    if value == len(random_list) - 1:
        print("|")

# 최소값, 중간값, 최댓값 저장
min_value = sort_list[0]
middle_value = sort_list[len(sort_list) // 2]
max_value = sort_list[len(sort_list) - 1]
# print(min_value, middle_value, max_value)
        
# 열 형식으로 출력
print("-" * 25)
print("열")
print("| 최소값 |", end=" ")
for value in range(5):
    line_min = 99
    for subvalue in range(len(random_list)):
        if subvalue % 5 == 0 and subvalue != 24 or subvalue == 0:
            
            if random_list[subvalue + value] < line_min:
                line_min = random_list[subvalue + value]
    if line_min < 10:
        print(line_min, end="  | ")
    else :
        print(line_min, end=" | ")
print("")
print("| 최대값 |", end=" ")
for value in range(5):
    line_max = 0
    for subvalue in range(len(random_list)):
        if subvalue % 5 == 0 and subvalue != 24 or subvalue == 0:
            
            if random_list[subvalue + value] > line_max:
                line_max = random_list[subvalue + value]
    print(line_max, end=" | ")
print("")
print("| 중간값 |", end=" ")
for value in range(5):
    line_list = []
    for subvalue in range(len(random_list)):
        if subvalue % 5 == 0 and subvalue != 24 or subvalue == 0:
            line_list.append(random_list[subvalue + value])
    line_list.sort()
    line_middle = line_list[len(line_list) // 2]
    if line_middle < 10:
        print(line_middle, end="  | ")
    print(line_middle, end=" | ")
print("")
    
# 행 형식으로 출력
print("-" * 25)
print("행")
print("| 최소값 | 최대값 | 중간값 |")
for value in range(5):
    line_min = 99
    line_max = 0
    line_list = []
    for subvalue in range(5):
        now = random_list[value * 5 + subvalue]
        if now < line_min:# 최소
            line_min = now
        elif now > line_max:# 최대
            line_max = now
        line_list.append(now)
    line_list.sort()
    line_middle = line_list[len(line_list) // 2] # 중간
    # 출력
    if line_min < 10:# 줄맞춤
        print("|  ", line_min, end="    ")
    else:
        print("|  ", line_min, end="   ")
    print("|  ", line_max, end="   ")
    if line_middle < 10:# 줄맞춤
        print("|  ", line_middle, end="    |")
    else:
        print("|  ", line_middle, end="   |")
    print("")
    
# 전체 값에 대한 최소, 중간, 최대값 출력
print("-" * 25)
print("전체")
print("| 최소값 |", min_value, " |")
print("| 최대값 |", max_value, "|")
print("| 중간값 |", middle_value, "|")