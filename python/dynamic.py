# n/층 다이나믹탱크에 필요한 강철의 수
# 구하는 계산기
# 블럭4개 당 4개의 강철
# 구조물용유리와 탱크블럭은 구분 안함
# 다이나믹탱크블럭 4개당  벨브 2개산출

import os

flagAll = True
while flagAll:
    flag1 = True
    flag2 = True
    value = int(input("층 수를 입력하시오.(최소 3, 최대 18)\n"))
    x = int(input("가로 입력(최소 3, 최대 18)\n"))
    z = int(input("세로 입력(최소 3, 최대 18)\n"))
    valve = int(input("밸브 갯수 입력(최소 2)\n"))
    xz = x * z
    steel = 0 # 강철변수
    for height in range (value):
        steel += xz
    steel -= valve
    steel += valve * 4
    Rsteel = steel # 실 강철 수
    print("------------------------------------------")
    print("총", steel, "개")
    print(steel // 64, "세트 /", steel % 64, "개")
    while flag1:
        if steel % 4 == 0 :
            flag1 = False
        else :
            steel += 1
    print("조합 시 ", steel, "개 필요", "(" + str(steel - Rsteel), "개 남음)")
    print("------------------------------------------")
    while flag2:
        cal = int(input("프로그램을 재사용할려면 1\n윈도우 계산기를 사용할려면 2\n프로그램을 종료할려면 3\n"))
        if cal == 1 :
            print("------------------------------------------")
            flag2 = False

        elif cal == 2 :
            print("------------------------------------------")
            os.system("calc.exe")
            
        elif cal == 3:
            print("------------------------------------------")
            flag2 = False
            flagAll = False
        else :
            print("------------------------------------------")
            print("재입력")

os.system("pause")