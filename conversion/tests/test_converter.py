import unittest
import pytest

from converter.convert_inputs import convert_to_roman


class TestRangeConvertion(unittest.TestCase):
    def number_out_of_range(self):
        with self.assertRaises(OutOfRangeError):
            convert_to_roman(5000)