floor = int(input("input floor"))

for basevalue in range(floor * 2):
    
    width_upper_value = basevalue * 2 + 1
    width_under_value = (floor * 4) - width_upper_value
    
    if basevalue < floor:
        for air in range(floor - basevalue):
            print(" ", end="")
            
        for subvalue in range(width_upper_value):
            if basevalue == floor - 1 or subvalue == 0 or subvalue == width_upper_value - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    
    elif basevalue > floor:
        for air in range((basevalue + 1) - floor):
            print(" ", end="")
            
        for subvalue in range(width_under_value):
            if subvalue == 0 or subvalue == width_under_value - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")