import unittest


from duplicate_index import duplicate_indexes


class TestDuplicateIndexes(unittest.TestCase):


    def test_that_duplicate_indexes_are_in_the_list(self):
        actual = duplicate_indexes([-11, -9, 3, -9, 2, -11])
        expected = [[-11, [0, 5]], [-9, [1, 3]]]
        self.assertEqual(actual, expected)


    def test_duplicate_indexes_with_number_zero(self):
        actual = duplicate_indexes([0, 2, 4, 2, 0, 0, 2])
        expected = [[0, [0, 4, 5]], [2, [1, 3, 6]]]
        self.assertEqual(actual, expected)

    def test_that_no_duplicate_in_any_indexes(self):
        actual = duplicate_indexes([0, 1, 2, 3, 4, 5])
        expected = []
        self.assertEqual(actual, expected)
