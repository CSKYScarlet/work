package main

import "fmt"

func multi_table(num_arg int) {
	for value := 2; value <= 9; value++ {
		println(num_arg, "X", value, "=", num_arg*value)
	}
}

func line() {
	for value := 1; value <= 20; value++ {
		print("-")
	}
	println()
}

func main() {
	var flag bool
	flag = true
	for flag == true {
		sel := 0

		line()
		println("1. 구구단 출력")
		println("2. 프로그램 종료")
		line()

		fmt.Scanln(&sel)

		if sel == 1 {
			num := 0
			println("출력할 구구단의 단을 입력하세요. 구구단의 단은 2~9 사이 입력")
			fmt.Scanln(&num)
			for true {
				if num >= 2 && num <= 9 {
					multi_table(num)
					break
				} else {
					println("2~9사이 정수를 입력해 주세요")
					fmt.Scanln(&num)
				}
			}

		} else if sel == 2 {
			print("이용해 주셔서 감사합니다.")
			flag = false
		} else {
			println("잘못 입력하셨습니다. 다시 입력하세요.")
		}
	}
}
