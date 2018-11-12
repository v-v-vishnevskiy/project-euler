package main

import (
	"fmt"
	"os"
)

func sum_of_even_fibonacci_terms(limit int) int {
	var result int
	var old_current int
	prev := 1
	current := 1

	for current < limit {
		old_current = current
		current += prev
		prev = old_current
		if current%2 == 0 {
			result += current
		}
	}
	return result
}

func test_time() int {
	result := 0
	for i := 0; i < 100000; i++ {
		result = sum_of_even_fibonacci_terms(4000000)
	}
	return result
}

func main() {
	if len(os.Args) > 1 {
		fmt.Println(test_time())
	} else {
		fmt.Println(sum_of_even_fibonacci_terms(4000000))
	}
}
