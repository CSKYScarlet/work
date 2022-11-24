package main

func main() {
	N := 5
	for height := 1; height <= 3; height++ {
		for value := 1; value <= N; value++ {
			for subvalue := 1; subvalue <= N; subvalue++ {
				print("*")
			}
			println()
		}
		println()
	}
}
