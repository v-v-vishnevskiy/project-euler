import unittest
from . import (
    solution_1,
    solution_2
)


class Solutions(unittest.TestCase): 
    
    def test_1(self):
        self.assertEqual(solution_1.solution(), 233168)

    def test_2(self):
        self.assertEqual(solution_2.solution(), 4613732)
