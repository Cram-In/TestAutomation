from converter.utilities import *

numeralMap = (
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
)


def convert_to_roman(num):
    if int(num) != num:
        raise ValueError("Not integer")
    if not (0 < num < 5000):
        raise OutOfRangeError("number out of range (must be 1..4999)")

    result = ""
    for roman, arabic in numeralMap:
        while num >= arabic:
            result += roman
            num -= arabic
    return result