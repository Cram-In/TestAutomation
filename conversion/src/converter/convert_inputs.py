from converter.utilities import *


def convert_to():
    display(operation_list)
    operation = int(input("Please select acction: "))
    print(operation)

    while True:
        # check input
        if operation not in allowed_operactions:
            print("Operation not allowed. Try again.")
            convert_to()
        # to roman
        if operation == 1:
            print("Convert to Roman")
            convert_to_roman(num)
        # to arabic
        elif operation == 2:
            print("Convert to Arabic")
            convert_to_arabic(num)


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


def convert_to_arabic(num):
    pass