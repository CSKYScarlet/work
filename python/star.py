floorvalue = int(input("층 수 입력"))
star = -1
starmsg = "*"
air = floorvalue
airmsg = " "
for value in range(air - 1):
    print(airmsg, end="")
print(floorvalue)
for value in range(floorvalue):
    star += 2
    air -= 1
    for value in range(air):
        print(airmsg, end="")
    for value in range(star):
        print(starmsg, end="")
    print("")