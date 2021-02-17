import roman
from converter.utilities import *

# convertion option selection
def convert_to(operation):
    # check input
    if operation not in allowed_operations:
        raise InputError("Operation not allowed. Try again.")
    # to roman
    if operation == 1:
        print("Convert to Roman")
        convert_to_roman(num)
    # to arabic
    elif operation == 2:
        print("Convert to Arabic")
        convert_to_arabic(string)


# arabic to roman
def convert_to_roman(num):
    if int(num) != num:
        raise ValueError("Not integer")
    if not (0 < num < 4000):
        raise ValueError("number out of range (must be 1..3999)")

    result = ""
    for roman, arabic in numeralMap:
        while num >= arabic:
            result += roman
            num -= arabic
    return result


# roman to arabic
def convert_to_arabic(string):
    if string != string.upper():
        raise InputError("Input must be in Upper Cases")
    if ValidationOfRomanNumerals(string):
        arabic_number = roman.fromRoman(string)
        return arabic_number
    else:
        raise ValueError("invalid roman numeral")