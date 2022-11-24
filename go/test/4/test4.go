package main

import (
	"strconv"
	"strings"
)

func main() {
	for value := 1; value <= 100; value++ {
		num := strconv.Itoa(value)
		list := strings.Split(num, "")
		for str := range list {
			if list[str] == "3" {
				println(num)
				break
			}
		}
	}
}
