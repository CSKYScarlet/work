floor = int(input("높이를 입력"))
width = int(input("넓이를 입력"))

for basevalue in range(floor):
    for air in range(basevalue):
        print(" ", end="")
        
    width_value = (floor * 2 + width) - ((basevalue * 2) + 1) - 1
    for subvalue in range(width_value):
        if basevalue == 0 or basevalue == floor - 1 or subvalue == 0 or subvalue == width_value - 1:
            print("*", end="")
        else:
            print(" ", end="")
            
    print("")