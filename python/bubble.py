from random import *

def random_def (N, MIN, MAX):
    num = []
    while len(num) != N:
        rand_value = randint(MIN, MAX)
        if rand_value not in num:
            num.append(rand_value)
    return num

def sort (listValue):
    for value in range(len(listValue)):
        for subvalue in range(len(listValue) - value - 1):
            # 현재 값이 다음 값보다 클 경우
            if listValue[subvalue] > listValue[subvalue + 1]:
                # 현재 위치의 값 킵
                temp = listValue[subvalue]
                # 현재 위치에 다음 값을 저장
                listValue[subvalue] = listValue[subvalue + 1]
                # 다음 위치에 킵 값 저장
                listValue[subvalue + 1] = temp
    return listValue
            
mylist = random_def(5, 1, 10)
print(mylist)
sortlist = sort(mylist)
print(sortlist)