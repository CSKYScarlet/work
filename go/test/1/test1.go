package main

import "fmt"

func main() {
	var input int
	var sum int
	N := 5
	for value := 1; value <= N; value++ {
		print(value, "번째 값 입력")
		fmt.Scanln(&input)
		sum += input
	}
	arv := (sum / N)
	println("합계 : ", sum)
	println("평균 : ", arv)
}
