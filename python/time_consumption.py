import sys
import time

import solution_1
import solution_2


def time_consumption(fn, solution_number: str, iterations: int) -> float:
    t1 = time.monotonic()
    for _ in range(iterations):
        fn()
    t2 = time.monotonic()
    print("{}: {:.3f}s".format(solution_number, t2 - t1))
    return t2 - t1


if __name__ == "__main__":
    print("Python", sys.version)
    total = 0
    total += time_consumption(solution_1.solution, "1", 10_000)
    total += time_consumption(solution_2.solution, "2", 100_000)
    print("Total: {:.3f}s".format(total))
