# 검사 상수(키값) 지정
key_list = []# 키값 저장용
for value in range(2, 14):# 키값 저장
    if value >= 10:
        key_list.append(value % 10 + 2)
    else:
        key_list.append(value)

# 주민번호 입력받기
user_num = input("주민번호 13자리를 입력하세요")

# 주민번호 판별 후 (리스트)저장
user_list = [] # 리스트 저장용
for value in user_num:
    if value.isdigit():
        user_list.append(int(value))

# 리스트와 키값 비교계산
cal_sum = 0
for value in range(12):
    # 곱셈, 덧셈
    cal_sum += (key_list[value] * user_list[value])

# 체크 계산
check_value = 11 - (cal_sum % 11)
if check_value >= 10:
    check_value = check_value % 10
# 유효 여부 판별
if check_value == user_list[12]:
    print("유효한 주민번호 입니다.")
else:
    print("유효하지 않은 주민번호 입니다.")