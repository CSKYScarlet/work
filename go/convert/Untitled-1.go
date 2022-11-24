package main

import (
	"fmt"
	"reflect"
	"strconv"
	"strings"
)

func main() {
	num := 123
	msg := strconv.Itoa(num)
	print(num)
	fmt.Printf(" %s\n", reflect.TypeOf(num))
	print(msg)
	fmt.Printf(" %s\n", reflect.TypeOf(msg))

	array := strings.Split(msg, "")
	fmt.Printf(" %s\n", array[0])
}
