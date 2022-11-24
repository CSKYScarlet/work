# 줄 수 입력받기
line_num = int(input("입력 문자열의 줄(Line) 수를 입력하세요!"))

# 문자열 입력받기
word_list = []
for value in range(line_num):
    word_list.append(input(str(value + 1) + "번째 라인의 문자열을 입력하세요."))

# 검색할 문자열 입력받기
search_word = input("검색 할 문자열을 입력하세요.")

# 검색
search_line = []
search_count = 0
word_count = 0
for value in range(line_num):
    count = 0
    next_char = " "
    previous_char = " "
    for word in range(len(word_list[value])):
        next_char = " " if word == (len(word_list[value]) - 1) else word_list[value][word + 1]
        
        # 단어 카운트
        if word_list[value][word] != " " and next_char == " ":
            word_count += 1
        
        # print(previous_char,word_list[value][word], next_char)
        if count == 0 and search_word[count] == word_list[value][word] and previous_char == " ":
            count += 1
            
        elif search_word[count] == word_list[value][word] and count > 0:
            if count == (len(search_word) - 1) and next_char == " ":
                # print(value, word)
                search_count += 1
                if value + 1 not in search_line:
                    search_line.append(value + 1)

            else:
                count += 1
            
        else:
            count = 0
            
        previous_char = word_list[value][word]
        
# 결과출력
if search_count > 0:
    print(search_word + "를 찾았습니다.")
    print("검색된 라인 :", search_line)
    print("검색된 횟수", search_count)
    print("총 단어 수 :", word_count)