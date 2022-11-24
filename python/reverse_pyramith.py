floor = int(input("층 수 입력"))

for basevalue in range(floor): # top pyramith
    for air in range(basevalue + 1):
        print(" ", end="")
        
    mainvalue = (floor * 2 - 1) - (2 * basevalue)
    
    for value in range(mainvalue):
        if basevalue == 0 or value == 0 or value == mainvalue - 1:
            print("*", end="")
        else :
            print(" ", end="")
    print("")
   
for value in range(3): # middle line
    if value == 1:
        for basevalue in range(floor * 2):
            print("*", end="")
        print("")
    else :
        for basevalue in range(floor * 2):
            print(" ", end="")
        print("")
        
for basevalue in range(floor): # bottom pyramith
    for air in range(floor - basevalue):
        print(" ", end="")
        
    mainvalue = 2 * basevalue + 1
    
    for value in range(mainvalue):
        if value == 0 or value == mainvalue - 1 or basevalue == floor - 1:
            print("*", end="")
        else :
            print(" ", end="")
    print("")