import unittest
import pytest

from converter.convert_inputs import convert_to_roman
from converter.utilities import *

test_cases = {5: "V", 4: "IV", 9: "IX", 11: "XI", 90: "XC", 110: "CX", 777: "DCCLXXVII"}


def test_number_out_of_range():
    with pytest.raises(OutOfRangeError):
        convert_to_roman(5000)


def test_number_not_ingeger():
    with pytest.raises(ValueError):
        convert_to_roman("Ala Ma Kota")


class TestFinalConvertion(unittest.TestCase):
    def test_converting_to_roman(self):
        for num, result in test_cases.items():
            self.assertEqual(convert_to_roman(num), result)
