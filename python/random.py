import random

random_range = int(input("랜덤을 돌릴 횟수"))
num_value = int(input("랜덤의(최대) 범위"))

# ran_num = random.randrange(1, (num_value + 1))
# print(ran_num)

def random_things():
    random_value = random.randrange(1, (num_value + 1))
    return random_value
    
sub_num = 0
list_num = [0]
rerandom = 0
for value in range(random_range):
    
    ran_num = random_things()
    for list_value in list_num:
        if list_value == ran_num:
            rerandom += 1
            print(rerandom, "번 다시 돌림", "(" + str(ran_num) + ")")
            break
    # if sub_num == ran_num:
    #     ran_num = random_things()
        
    if list_value == ran_num:
        continue
    print(ran_num)
    list_num.append(ran_num)