import unittest

from shift_cipher import encrypt_caesar


class TestShiftCipher(unittest.TestCase):


    def test_that_uppercase_message_is_encrypted(self):
        actual = encrypt_caesar("HOW ARE YOU DOING TODAY!", 20)
        expected = ("BIQ ULY SIO XICHA NIXUS!")
        self.assertEqual(actual, expected)


    def test_that_lowercase_message_is_encrypted(self):
        actual = encrypt_caesar("hello can you dash me one million naira", 6)
        expected = ("nkrru igt eua jgyn sk utk sorrout tgoxg")
        self.assertEqual(actual, expected)

    def test_that_i_want_to_marry_a_software_engineer_like_myself(self):
        actual = encrypt_caesar("i want to marry a software engineer like myself", 10)
        expected = ("s gkxd dy wkbbi k cypdgkbo oxqsxoob vsuo wicovp")
        self.assertEqual(actual, expected)

