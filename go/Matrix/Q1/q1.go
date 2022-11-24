package main

import "fmt"

func main() {
	num := 0
	print("양의 정수를 입력 하세요")
	fmt.Scanln(&num)
	for value := 1; value <= num; value++ {
		for subvalue := 1; subvalue <= value; subvalue++ {
			print(subvalue, " ")
		}
		println()
	}
}
