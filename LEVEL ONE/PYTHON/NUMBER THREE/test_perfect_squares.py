import unittest

from perfect_squares import get_perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_provided_example(self):
        my_numbers = [4, 7, 9, 10, 16, 18]
        expected = [4, 9, 16]
        actual = get_perfect_squares(my_numbers)
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        test_list = []
        expected = []
        actual = get_perfect_squares(test_list)      
        self.assertEqual(actual, expected)

