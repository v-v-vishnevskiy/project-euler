package main

import (
	"fmt"
	"os"
)

func sum_of_multiples_of_3_and_5(limit int) int {
	result := 0
	for i := 0; i < limit; i++ {
		if i%3 == 0 || i%5 == 0 {
			result += i
		}
	}
	return result
}

func time_test() int {
	result := 0
	for i := 0; i < 10000; i++ {
		result = sum_of_multiples_of_3_and_5(1000)
	}
	return result
}

func main() {
	if len(os.Args) > 1 {
		fmt.Println(time_test())
	} else {
		fmt.Println(sum_of_multiples_of_3_and_5(1000))
	}
}
