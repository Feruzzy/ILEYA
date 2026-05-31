import unittest
from check_out_function import calculate_bill_total, calculate_balance


class TestCheckOutApp(unittest.TestCase):

    def test_that_bill_total_is_calculated_correctly_without_discount(self):
        sub_total = 10000
        discount = 0
        actual = calculate_bill_total(sub_total, discount)
        expected = 11750.0 
        self.assertEqual(actual, expected)

    def test_that_bill_total_is_calculated_correctly_with_10_percent_discount(self):
        sub_total = 10000
        discount = 10
        actual = calculate_bill_total(sub_total, discount)
        expected = 10750.0  
        self.assertEqual(actual, expected)

    def test_that_bill_total_is_calculated_correctly_with_20_percent_discount(self):
        sub_total = 20000
        discount = 20
        actual = calculate_bill_total(sub_total, discount)
        expected = 19500.0 
        self.assertEqual(actual, expected)

    def test_that_balance_is_calculated_correctly(self):
        amount_paid = 15000
        bill_total = 11750
        actual = calculate_balance(amount_paid, bill_total)
        expected = 3250
        self.assertEqual(actual, expected)

    def test_that_balance_is_zero_when_exact_amount_is_paid(self):
        amount_paid = 11750
        bill_total = 11750
        actual = calculate_balance(amount_paid, bill_total)
        expected = 0
        self.assertEqual(actual, expected)

