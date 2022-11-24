package main

func main() {
	N := 5
	for value := 1; value <= N; value++ {
		for subvalue := 1; subvalue <= N; subvalue++ {
			if subvalue >= value {
				print("*")
			} else {
				print(" ")
			}
		}
		println("")
	}
}
