from converter.utilities import *

# convertion option selection
def convert_to():
    display(operation_list)
    operation = int(input("Please select acction: "))
    print(operation)

    while True:
        # check input
        if operation not in allowed_operactions:
            raise InputError("Operation not allowed. Try again.")
            convert_to()
        # to roman
        if operation == 1:
            print("Convert to Roman")
            convert_to_roman(num)
        # to arabic
        elif operation == 2:
            print("Convert to Arabic")
            convert_to_arabic(num)


# arabic to roman
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


# roman to arabic
def convert_to_arabic(string):
    if string != string.upper():
        raise InputError("Input must be in Upper Cases")
    if ValidationOfRomanNumerals(string):
        pass
    else:
        raise InvalidRomanNumeralError("invalid roman numeral")