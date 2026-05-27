import unittest

from array_split import split_numbers

class TestSplitNumbers(unittest.TestCase):


    def test_that_this_list_of_numbers_is_splitted(self):
        actual = split_numbers([45, 60, 3, 10, 9, 22])
        expected = ([60, 10, 22], [45, 3, 9])
        self.assertEqual(actual, expected)

    def test_list_numbers(self):
        actual = split_numbers([3, 40, 5, 4, 9, 77])
        expected = ([40, 4], [3, 5, 9, 77])
        self.assertEqual(actual, expected)


