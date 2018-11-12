import sys


def sum_of_even_fibonacci_terms(limit: int) -> int:
    result = 0
    prev = 1
    current = 1
    while current < limit:
    	old_current = current
    	current = current + prev
    	prev = old_current
    	if current % 2 == 0:
    		result += current
    return result


def time_test():
    result = None
    for _ in range(100_000):
        result = sum_of_even_fibonacci_terms(4_000_000)
    print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1: 
        time_test()
    else:
        print(sum_of_even_fibonacci_terms(4_000_000))
