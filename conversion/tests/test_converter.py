import unittest
import pytest

from converter.convert_inputs import convert_to_roman, convert_to_arabic, convert_to
from converter.utilities import *


# roman converter tests
test_cases = {5: "V", 4: "IV", 9: "IX", 11: "XI", 90: "XC", 110: "CX", 777: "DCCLXXVII"}


def test_number_out_of_range():
    with pytest.raises(OutOfRangeError):
        convert_to_roman(5000)


def test_number_not_ingeger():
    with pytest.raises(ValueError):
        convert_to_roman("Ala Ma Kota")


class TestFinalConvertionToRoman(unittest.TestCase):
    def test_converting_to_roman(self):
        for num, result in test_cases.items():
            self.assertEqual(convert_to_roman(num), result)


# arabic converter tests


def test_if_input_upper():
    with pytest.raises(InputError):
        convert_to_arabic("ii")


def test_if_valid_roman_num():
    with pytest.raises(InvalidRomanNumeralError):
        convert_to_arabic("MMMM")


class TestFinalConvertionToArabic(unittest.TestCase):
    def test_converting_to_arabic(self):
        for result, string in test_cases.items():
            self.assertEqual(convert_to_arabic(string), result)


# selection tests
