import unittest

from duplicate_numbers import duplicates



class TestFunctions(unittest.TestCase):

    def test_find_duplicates_numbers(self):
        actual = duplicates([1, 2, 3, 2, 4, 3])
        expected = [2, 3]
        self.assertEqual(actual, expected)

    def test_that_the_list_has_duplicate_numbers_like_zero(self):
        actual = duplicates([0, 2, 3, 0, 0, 3, 5])
        expected = [0, 3]
        self.assertEqual(actual, expected)

    def test_that_no_duplicate_numbers(self):
        actual = duplicates([2, 3, 4, 5, 6, 7])
        expected = []
        self.assertEqual(actual, expected)

