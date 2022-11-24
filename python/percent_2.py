import random

def def_percents(percent):
    num = random.randint(1, 100)
    if num > 100 - percent:
        return True
    
count = 1
while True:
    
    boolean = def_percents(1)
    if boolean == True:
        print(boolean, count)
        break

    count += 1