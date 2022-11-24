package main

import "fmt"

func main() {
	num := 0
	fmt.Scanln(&num)
	if num >= 95 {
		println("A+")
	} else if num >= 90 {
		println("A")
	} else if num >= 85 {
		println("B+")
	} else if num >= 80 {
		println("B")
	} else if num >= 75 {
		println("C+")
	} else if num >= 70 {
		println("C")
	} else if num >= 65 {
		println("D+")
	} else if num >= 60 {
		println("D")
	} else {
		println("F")
	}
}
