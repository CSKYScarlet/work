# 입력된 넓이 값에 따른 사다리꼴 피라미드 출력

floor = int(input("높이 입력"))
width  = int(input("넓이(윗변) 입력"))

if width == 0 or floor == 0:
    pass
else:
    for basevalue in range(floor):
        for air in range(floor - basevalue):
            print(" ", end="")
            
        width_value = (basevalue * 2) + width
        for subvalue in range(width_value):
            if basevalue == 0 or basevalue == floor - 1 or subvalue == 0 or subvalue == width_value - 1:
                print("*", end="")
            else:
                print(" ", end="")
                
        print("")