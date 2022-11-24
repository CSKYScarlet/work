package main

func main() {
	N := 5
	for repeat := 1; repeat <= 2; repeat++ {
		for value := 1; value <= N; value++ {
			for subvalue := 1; subvalue <= N; subvalue++ {
				if (repeat == 1 && value%2 == 0 && subvalue%2 == 0) || (repeat == 2 && subvalue == value) {
					print(" ")
				} else {
					print("*")
				}
			}
			println()
		}
		println()
	}
}
