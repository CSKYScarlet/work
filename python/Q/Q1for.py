num  = int(input("양의 정수를 입력 하세요"))

for basevalue in range(num):
    for subvalue in range(basevalue + 1):
        print(subvalue + 1, end="")
    print("")