flag = True

run_num = 0
while flag:
    msg_num = ""
    num = int(input(""))
    
    if num > 0 and num != 20000:
        run_num += 1
        if num % 2 == 0:
            msg_num = "짝수"
        elif num % 2 == 1:
            msg_num = "홀수"
        print(run_num, "번째 입력 값은 = ", num)
        print("\t\t", msg_num, "입니다.")
        
        if num % 3 == 0:
            print("\t\t", "3의 배수 입니다.")
        if num % 7 == 0:
            print("\t\t", "7의 배수 입니다.")
            
    elif num <= 0:
        print("1이상 양수를 입력해 주세요")
    
    if num == 20000:
        print("이용해주셔서 감사합니다")
        flag = False