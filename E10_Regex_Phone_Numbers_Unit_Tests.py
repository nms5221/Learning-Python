'''
Unit Testing for Validate Data for Phone Numbers
https://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/
'''

import unittest
from E10_Regex_Phone_Numbers.py import validate_phone_number


class test_phone_number(unittest.TestCase):
    def test_only_numbers_eleven_digits(self):
        x = '12345678900'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_only_numbers_ten_digits(self):
        x = '1234567890'
        expected = True
        self.assertEquals(validate_phone_number(x), expected)

    def test_only_numbers_nine_digits(self):
        x = '123456789'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_only_numbers_eight_digits(self):
        x = '12345678'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_only_numbers_seven_digits(self):
        x = '1234567'
        expected = True
        self.assertEquals(validate_phone_number(x), expected)

    def test_only_numbers_six_digits(self):
        x = '123456'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_dashes_ten_digits_valid(self):
        x = '123-456-7890'
        expected = True
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_dashes_ten_digits_not_valid(self):
        x = '123-45-67890'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_dashes_seven_digits_valid(self):
        x = '123-4567'
        expected = True
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_dashes_seven_digits_not_valid(self):
        x = '1234-567'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_dots_ten_digits_valid(self):
        x = '123.456.7890'
        expected = True
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_dots_ten_digits_not_valid(self):
        x = '123.45.67890'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_dots_seven_digits_valid(self):
        x = '123.4567'
        expected = True
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_dots_seven_digits_not_valid(self):
        x = '1234.567'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_spaces_ten_digits_valid(self):
        x = '123 456 7890'
        expected = True
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_spaces_ten_digits_not_valid(self):
        x = '123 45 67890'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_extra_spaces_ten_digits_not_valid(self):
        x = '123  456  7890'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_spaces_seven_digits_valid(self):
        x = '123 4567'
        expected = True
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_spaces_seven_digits_not_valid(self):
        x = '1234 567'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_extra_spaces_seven_digits_not_valid(self):
        x = '123  4567'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_parenthesis_ten_digits_valid(self):
        x = '(123)4567890'
        expected = True
        self.assertEquals(validate_phone_number(x), expected)

    def test_numbers_with_parentheses_ten_digits_not_valid(self):
        x = '(1234567890'
        expected = False
        self.assertEquals(validate_phone_number(x), expected)


if __name__ == '__main__':
    unittest.main()
