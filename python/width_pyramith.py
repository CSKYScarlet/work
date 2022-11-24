num = 11

Rnum = round(num / 2) + 1
for basevalue in range(num):
    if basevalue < Rnum - 1:
        for subvalue in range(basevalue + 1):
                print("*", end="")
    else:
        for subvalue in range(num - basevalue):
            print("*", end="")
    print("")