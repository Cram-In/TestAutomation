from converter.utilities import *


def convert_to_roman(num):
    if int(num) != num:
        raise ValueError("Not integer")
    if not (0 < num < 5000):
        raise OutOfRangeError("number out of range (must be 1..4999)")
