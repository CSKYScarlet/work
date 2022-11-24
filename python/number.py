# 입력 된 숫자를 그림으로 출력하는 프로그램

number = input("수를 입력(값 제한 無)")

numheigh = 5
numwidth = 5
for value in number: # 입력 된 값을 순서대로 루팅
    if value == "0" : # 현재 값이 "0" 일경우 0 출력
        for mainnumvalue in range(numheigh):
            for numvalue in range(numwidth):
                # (첫 라인 또는 마지막 라인의 (첫번째 이거나 마지막) 일 경우) 공백출력
                if ((mainnumvalue == 0 or mainnumvalue == numheigh - 1) and (numvalue == 0 or numvalue == numwidth - 1)):
                    print(" ", end="")
                
                # (첫 라인 또는 마지막 라인의 (첫번째 가 아니며 마지막)이 아닐 경우)별 출력
                # (첫 라인 또는 마지막 라인이 아니며 (첫번째 이거나 마지막) 일 경우) 별 출력
                elif ((((mainnumvalue == 0 or mainnumvalue == numheigh - 1) and (numvalue != 0 or numvalue != numwidth - 1))) or (((mainnumvalue != 0 or mainnumvalue != numheigh - 1) and (numvalue == 0 or numvalue == numwidth - 1)))):
                    print("*", end="")
                    
                # 그 외 공백 출력(내부)
                else :
                    print(" ", end="")
            print("")
    
    if value == "1": # 현재 값이 "1" 일 경우 1 출력
        for mainnumvalue in range(numheigh):
            for numvalue in range(numwidth):
                if (mainnumvalue == 0 and numvalue == 1) or (mainnumvalue == 1 and numvalue == 0) or numvalue == 2 or mainnumvalue == numheigh - 1:
                    print("*", end="")
                else :
                    print(" ", end="")
            print("")
            
    if value == "2": # 현재 값이 "2" 일 경우 2 출력
        for mainnumvalue in range(numheigh):
            for numvalue in range(numwidth):
                if (mainnumvalue == 0 and (numvalue == 1 or numvalue == 2 or numvalue == 3)) or (mainnumvalue == 1 and (numvalue == 0 or numvalue == numwidth - 1)) or (mainnumvalue == 2 and numvalue == numwidth - 2) or (mainnumvalue == 3 and numvalue == numwidth - 3) or (mainnumvalue == numheigh - 1):
                    print("*", end="")
                else :
                    print(" ", end="")
            print("")
    
    if value == "3": # 현재 값이 "3" 일 경우 3 출력
        for mainnumvalue in range(numheigh):
            for numvalue in range(numwidth):
                if (mainnumvalue != 1 and mainnumvalue != 3) or (numvalue == 4 and (mainnumvalue == 1 or mainnumvalue == 3)):
                    print("*", end="")
                else :
                    print(" ", end="")
            print("")
            
    if value == "4": # 현재 값이 "4" 일 경우 4 출력
        for mainnumvalue in range(numheigh):
            for numvalue in range(numwidth):
                if numvalue == 3 or mainnumvalue == 3 or (mainnumvalue == 0 and numvalue == 2) or (mainnumvalue == 1 and numvalue == 1) or (mainnumvalue == 2 and numvalue == 0):
                    print("*", end="")
                else :
                    print(" ", end="")
            print("")
            
    if value == "5": # 현재 값이 "5" 일 경우 5 출력
        for mainnumvalue in range(numheigh):
            for numvalue in range(numwidth):
                if (mainnumvalue != 1 and mainnumvalue != 3) or (mainnumvalue != 3 and numvalue == 0) or (mainnumvalue != 1 and numvalue == 4):
                    print("*", end="")
                else :
                    print(" ", end="")
            print("")
            
    if value == "6": # 현재 값이 "6" 일 경우 6 출력
        for mainnumvalue in range(numheigh):
            for numvalue in range(numwidth):
                if ((mainnumvalue != 1 and mainnumvalue != 3) and (numvalue != 0 and numvalue != 4)) or ((mainnumvalue != 0 and mainnumvalue != 4) and numvalue == 0) or (mainnumvalue == 3 and numvalue == 4):
                    print("*", end="")
                else :
                    print(" ", end="")
            print("")
            
    if value == "7": # 현재 값이 "7" 일 경우 7 출력
        for mainnumvalue in range(numheigh):
            for numvalue in range(numwidth):
                if mainnumvalue == 0 or numvalue == 4 or (numvalue == 0 and (mainnumvalue != 3 and mainnumvalue != 4)):
                    print("*", end="")
                else :
                    print(" ", end="")
            print("")
            
    if value == "8": # 현재 값이 "8" 일 경우 8 출력
        for mainnumvalue in range(numheigh):
            for numvalue in range(numwidth):
                if ((numvalue != 0 and numvalue != 4) and (mainnumvalue != 1 and mainnumvalue != 3)) or ((numvalue == 0 or numvalue == 4) and (mainnumvalue == 1 or mainnumvalue == 3)):
                    print("*", end="")
                else :
                    print(" ", end="")
            print("")
    
    if value == "9": # 현재 값이 "9" 일 경우 9 출력
        for mainnumvalue in range(numheigh):
            for numvalue in range(numwidth):
                if ((mainnumvalue != 1 and mainnumvalue != 3) and (numvalue != 0 and numvalue != 4)) or (mainnumvalue == 1 and numvalue == 0) or (numvalue == 4 and (mainnumvalue != 0 and mainnumvalue != 4)):
                    print("*", end="")
                else :
                    print(" ", end="")
            print("")
            
    print("■■■■■■■■■■")
    
print(number)