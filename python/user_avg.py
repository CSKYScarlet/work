def avg_def(list_arg):
    sum = 0
    num_count = 0
    for value in range(len(list_arg)):
        for subvalue in list_arg[value]:
            if type(subvalue) == int:
                sum += subvalue
                num_count += 1
                
    return sum / num_count

def prt_user(prt_arg):
    for value in range(len(prt_arg)):
        for subvalue in range(len(prt_arg[value])):
            if subvalue == 0:
                print("학번 :", prt_arg[value][subvalue], end="\t|\t")
            elif subvalue == 1:
                print("이름 :", prt_arg[value][subvalue], end="\t|\t")
            elif subvalue == 2:
                print("국어 :", prt_arg[value][subvalue], end="\t|\t")
            elif subvalue == 3:
                print("영어 :", prt_arg[value][subvalue], end="\t|\t")
            elif subvalue == 4:
                print("수학 :", prt_arg[value][subvalue], end="\t|\t")
        sum = prt_arg[value][2] + prt_arg[value][3] + prt_arg[value][4]
        print("합계 :", sum, end="\t|\t")
        print("평균 :", sum / 3)

#--------------------------------------------------
user_list = []
user_avg = 0

flag = True
while flag:
    print("==============================")
    print(" 1. 학생 성적 입력")
    print(" 2. 학생 목록 출력(입력 순)")
    print(" 3. 프로그램 종료")
    print("")
    print(" 현 입력데이터 갯수 :", len(user_list))
    print(" 전체 학생 평균 값 :", user_avg)
    print("==============================")
    option = int(input())
    
    if option == 1:
        user_num = input("학번을 입력하세요")
        user_name = input("이름을 입력하세요")
        kor = int(input("국어 성적을 입력하세요"))
        eng = int(input("영어 성적을 입력하세요"))
        math = int(input("수학 성적을 입력하세요"))
        profile = [user_num, user_name, kor, eng, math]
        user_list.append(profile)
        
        user_avg = avg_def(user_list)
    
    elif option == 2:
        prt_user(user_list)
        
    elif option == 3:
        print("프로그램 종료")
        flag = False