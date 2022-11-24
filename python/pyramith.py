# 층 수 입력받기
floorvalue = int(input("층 수 입력"))

# 변수 선언
star = 1
starmsg = "*"
air = floorvalue
air2 = -1
airmsg = " "
base = floorvalue - 1

# 반복문 실행
for basevalue in range(floorvalue - 1):
    air -= 1
    for value in range(air):
        print(airmsg, end="")
    print(starmsg, end="")
    
    # 중간공백 출력
    for value in range(air2):
        print(airmsg, end="")
    air2 += 2
        
    # 오른 변 별 출력
    if star >= 2 and star <= floorvalue:
        print(starmsg, end="")
    star += 1
    print("")
    
    # 바닥 출력
    if basevalue == floorvalue - 2:
        base = base + floorvalue
        for value in range(base):
            print("*", end="")
        break