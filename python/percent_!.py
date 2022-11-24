import random

def def_percents(percent):
    
    bit = []

    for value in range(int(((100 / percent) ** (1/2)))):
        bit.append(random.randint(0, 1))
        
    if 1 not in bit:
        return True
    
count = 1
true = 0
while True:
    
    boolean = def_percents(30)
    if boolean == True:
        print(boolean, count)
        break

    count += 1