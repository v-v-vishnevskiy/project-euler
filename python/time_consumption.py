import sys
import time

import solution_1
import solution_2


def time_consumption(fn, solution_number: str, iterations: int) -> float:
    total_time = 0
    for _ in range(iterations):
        t1 = time.monotonic()
        fn()
        total_time += (time.monotonic() - t1)
    print("{}: {:.3f}s".format(solution_number, total_time))
    return total_time


if __name__ == "__main__":
    print("Python", sys.version)
    total = 0
    total += time_consumption(solution_1.solution, "1", 10_000)
    total += time_consumption(solution_2.solution, "2", 100_000)
    print("Total: {:.3f}s".format(total))
