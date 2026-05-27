import unittest
from palindrome_checker import checking_palindrome

class TestPalindromeArrayChecker(unittest.TestCase):

    def test_valid_palindrome(self):
        actual = checking_palindrome([45, 0, 8, 0, 45])
        expected = True
        self.assertEqual(actual, expected)

    def test_invalid_palindrome(self):
        actual = checking_palindrome([1, 2, 3, 4, 5])
        expected = False
        self.assertEqual(actual, expected)

    def test_even_length_palindrome(self):
        actual = checking_palindrome([1, 2, 2, 1])
        expected = True
        self.assertEqual(actual, expected)

    def test_single_element(self):
        actual = checking_palindrome([7])
        expected = True
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        actual = checking_palindrome([])
        expected = True
        self.assertEqual(actual, expected)
