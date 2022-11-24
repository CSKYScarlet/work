mainvalue = int(input("input floor"))

def floorprint():

    floor = mainvalue
    
    for basevalue in range(floor):
        for air in range(floor - basevalue):
            print(" ", end="")
            
        cyclevalue = 2 * basevalue + 1
        for subvalue in range(cyclevalue):
            if basevalue == floor - 1 or subvalue == 0 or subvalue == cyclevalue - 1 or subvalue == (cyclevalue - subvalue) - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
        
    for basevalue in range(floor):
        if basevalue == 0:
            continue
        for air in range(basevalue + 1):
            print(" ", end="")
            
        cyclevalue = (floor * 2) - (2 * basevalue + 1)
        for subvalue in range(cyclevalue):
            if subvalue == 0 or subvalue == cyclevalue - 1 or subvalue == (cyclevalue - subvalue) - 1:
                print("*", end="")
            else:
                print(" ", end="")
                
        print("")
    
    return(print(floor))

floorprint()