import unittest

from credit_card_validator import validate_card

class TestCreditCardValidator(unittest.TestCase):

    def test_valid_visa_card(self):
        expected = ("Visa", 16, "Valid")
        actual = validate_card("4111111111111111")
        self.assertEqual(actual, expected)

    def test_american_express_card(self):
        expected = ("American Express", 15, "Invalid")
        actual = validate_card("370000000000000")
        self.assertEqual(actual, expected)

    def test_invalid_short_card(self):
        expected = ("Visa", 4, "Invalid")
        actual = validate_card("4111")
        self.assertEqual(actual, expected)


