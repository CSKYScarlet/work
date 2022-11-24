package main

import "fmt"

func main() {
	for {
		var input int
		print("정수를 입력하세요")
		fmt.Scanln(&input)
		if input > 0 {
			println("양수 입니다.")
		} else if input < 0 {
			println("음수 입니다.")
		} else {
			break
		}
	}
}
