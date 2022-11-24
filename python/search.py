# 영문 문자열을 키보드로부터 입력 받아 List에 저장 후, 검색 단어를 키보드로부터 다시
# 입력 받아 해당 단어가 있을 경우 결과 값 출력
#  1.1 사용자로부터(키보드) 입력 받을 문자열의 라인 수 입력 후 리스트에 저장
#  1.2 검색 할 단어를 키보드로부터 입력 받고, 찾는 문자열이 있을 경우 아래와 같이 출력
#       1.2.1 검색 된 단어 유/무 출력
#           찾는 문자열이 없을 경우 계속해서 검색 문자열 입력
#       1.2.2 검색 된 단어의 줄, 총 검색 횟수 출력
#  1.3 입력받은 문자열의 단어 개수 카운트 후 출력
#--------------------------------------------------------------------------------

# 입력 문자열의 줄 수 입력받기
from itertools import count


line_value = int(input("입력 문자열의 줄(Line) 수를 입력하세요!\n"))

# 줄 수 만큼 문자열 입력받기
line_list = [] # 리스트로 저장
# word_count_list = []
word_count = 0
search_list = []
for value in range(line_value):
    input_value = input(str(value + 1) + "번째 라인의 문자열을 입력하세요.\n")
    line_list.append(input_value)
    count = 0
    word_list = []
    for list_value in line_list[value]:
        # # 단어수 카운트
        # word_count_list.insert(0, list_value)
        # if len(word_count_list) > 2:
        #     if word_count_list[0] != " " and word_count_list[1] == " " and word_count_list[2] != " ":
        #         word_count += 1

        # 단어 리스트 작성
        if list_value != " ":
            word_list.append("")
            word_list[count] += list_value
        else:
            count += 1

    search_list.append(word_list)

# 검색할 문자열 입력받기
flag = False
while True:
    search = input("검색 할 문자열을 입력하세요.\n")
    for value in search_list:
        if search in value:
            flag = True
    # 없을 시 재입력 받기
    if flag == False:
        print("찾을 수가 없습니다.", end="")
        continue
    # 찾았을 경우 메시지 출력
    elif flag == True:
        print(search + "를 찾았습니다.")
        break

# 검색
search_line = []
search_count = 0
for value in range(line_value):
    if search in search_list[value]:
        search_line.append(value + 1)
        for subvalue in search_list[value]:
            if subvalue == search:
                search_count += 1

for value in search_list:
    for subvalue in value:
        if subvalue != "":
            word_count += 1
# 검색된 라인 수 출력
print("검색된 라인 수 :", search_line)
# 검색된 횟수 출력
print("검색된 횟수 :", search_count)
# 총 단어 수 출력
print("총 단어 수 :", word_count)