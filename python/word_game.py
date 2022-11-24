# 1. 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장
#  a) 단어의 글자 범위 :5이상, 20이하
#  b) 유효범위 이외 단어 입력 시 재입력

# 2. 입력된 3개의 단어 중 한 개 단어를 임의 선택

# 3. 게임 시작
#  a) 선택된 단어의 글자 중 50%를 Blind 처리, Blind 처리 알파벳은 랜덤하게 선택
#  b) 예) 지정된 단어가 starbucks 인 경우 [9 글자], 9/2 = 4.5 -> 올림 -> 5
#  올림 알고리즘은 직접 구현 (올림 예 : 2.1 -> 3)

from random import randint

# 반올림 함수
def half_up(word_arg):
    if len(word_arg) / 2 > len(word_arg) // 2:
        half = len(word_arg) // 2 + 1
    else:
        half = len(word_arg) // 2
    return half

# 단어 조합 함수
def word_sum(word_list_arg):
    return_word = ""
    for value in word_list_arg:
        return_word += value
    return return_word

#--------------------------------------------------------------

# 단어를 저장할 변수
input_words = []

# 단어 저장 루틴
N = 3
while len(input_words) != N:
    word = input(str(len(input_words) + 1) + "번째 단어를 입력 하세요\n")
    # 유효범위 확인 후 단어 저장
    if len(word) >= 5 and len(word) <= 20:
        input_words.append(word)
    else:
        print("5이상 20이하 글자로 구성된 단어를 입력 하세요")
print()

# 랜덤 단어 선택
random_word = input_words[randint(0, N - 1)]
print("단어 선택 완료 게임을 시작 합니다.")
# print("선택된 단어 :", random_word)
print()

# 선택된 단어의 절반 가리기
half = half_up(random_word)
hide_value = []
# 어떤 글자를 가릴지 선택
while len(hide_value) < half:
    random_value = randint(0, len(random_word) - 1)
    if random_value not in hide_value:
        hide_value.append(random_value)
        
# 선택된 단어를 리스트형식으로 저장
word_list = []
for value in random_word:
    word_list.append(value)
    
# 저장된 리스트 값 복사후 선택된 글자 가리기
hide_list = word_list.copy()
for value in hide_value:
    hide_list[value] = "_"

# print(word_list)
# print(hide_list)

# 시도 루틴
flag = True
count = 0
while flag:
    count += 1
    print(count, "번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.")
    hide_word = word_sum(hide_list)
    print(hide_word)
    print()
    input_value = input()
    print()
    
    # 포함 여부 판별
    if input_value not in word_list:
        print("단어 내 포함되지 않은 알파벳입니다.")
        print()
        
    else:
        # 포함 횟수 카운트
        math = 0
        for value in range(len(word_list)):
            if word_list[value] == input_value:
                math += 1
                hide_list[value] = input_value
                
    # Clear 여부 확인
    clear = 0
    for value in range(len(word_list)):
        if word_list[value] == hide_list[value]:
            clear += 1
    if clear == len(word_list):
        print("Clear - 선택된 단어 :", random_word, "총 시도 횟수 :", count)
        flag = False
        break
                
    if math > 0:
        print("입력한 알파벳 단어 내 포함 :", str(math) + "글자")