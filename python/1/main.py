import sys


def sum_of_multiples_of_3_and_5(limit: int) -> int:
    return sum((x for x in range(1, limit) if x % 3 == 0 or x % 5 == 0))


def time_test():
    result = None
    for _ in range(10000):
        result = sum_of_multiples_of_3_and_5(1000)
    print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1: 
        time_test()
    else:
        print(sum_of_multiples_of_3_and_5(1000))
