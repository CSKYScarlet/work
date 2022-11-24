package main

func main() {
	for value := 1; value <= 100; value++ {
		if value%8 == 0 {
			println(value)
		}
	}
}
