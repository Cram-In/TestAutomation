import unittest
import pytest

from converter.convert_inputs import convert_to_roman
from converter.utilities import *


def test_number_out_of_range():
    with pytest.raises(OutOfRangeError):
        convert_to_roman(5000)


def test_number_not_ingeger():
    with pytest.raises(ValueError):
        convert_to_roman("Ala Ma Kota")