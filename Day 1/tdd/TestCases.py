import unittest
from loan_calculator import loan_calculator


class Loan(unittest.TestCase):
    def test_month_is_not_greater_than_twelve(self):
        self.assertEquals(loan_calculator(100000, 11, 13), "Invalid Number of months!")

    def test_it_works(self):
        self.assertEquals(loan_calculator(100000, 12, 1), 112000)

    def test_loan_is_a_float(self):
        loan = loan_calculator(100000, 12, 1)
        self.assertIsInstance(loan, float, "The returned loan should be a float")

    def test_amount_is_not_negative(self):
        self.assertEquals(loan_calculator(-895, 12, 1), "Invalid amount!", "Loan amount should not be negative!")

    def test_rate_is_not_greater_than_hundred(self):
        self.assertEquals(loan_calculator(100000, 101, 13), "Invalid rate!")

if __name__=='__main__':
    unittest.main()
