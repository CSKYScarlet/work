package main

func main() {
	N := 4
	for value := 0; value <= N; value++ {
		for subvalue := 0; subvalue <= N; subvalue++ {
			if value == 0 || value == 4 || value == subvalue || N-value == subvalue {
				print("*")
			} else {
				print(" ")
			}
		}
		println()
	}
}
