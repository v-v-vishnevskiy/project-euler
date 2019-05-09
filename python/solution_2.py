"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def solution() -> int:
    limit = 4000000
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
