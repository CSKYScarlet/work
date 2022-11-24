num  = int(input("양의 정수를 입력 하세요"))

baseflag = True
subflag = True
basevalue = 0
subvalue = 0

while baseflag:
    basevalue += 1
    while subflag:
        print(subvalue + 1, end="")
        subvalue += 1
        if subvalue == basevalue:
            subflag = False
    subvalue = 0
    subflag = True
    print("")
    if basevalue == num:
        baseflag = False