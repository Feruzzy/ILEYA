import unittest


from moving_zero import move_zeros


class TestMovedZero(unittest.TestCase):

        def test_that_all_zeros_was_moved(self):
            actual = move_zeros([5, 0, 3, 0, 2, 0])
            expected = [5, 3, 2, 0, 0, 0]
            self.assertEqual(actual, expected)


        def test_that_zero_was_moved(self):
            actual = move_zeros([0, 2, 3, 4, 0, 9])
            expected = [2, 3, 4, 9, 0, 0]
            self.assertEqual(actual, expected)
