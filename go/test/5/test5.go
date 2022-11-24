package main

import "strings"

func main() {
	myList := "!! hello world, it is awesome day."
	msg := strings.Split(myList, " ")
	msgList := strings.Split(myList, "")

	Scount := 0
	Wcount := 0

	for value := range msgList {
		if msgList[value] == "!" || msgList[value] == "." || msgList[value] == "," {
			Scount++
		} else if msgList[value] != " " {
			Wcount++
		}
	}

	print("특수문자 수 : ", Scount, "\n")
	print("단어 수 : ", len(msg)-1, "\n")
	print("특수문자 제외 글자수 : ", Wcount, "\n")

}
