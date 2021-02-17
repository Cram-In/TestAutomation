class OutOfRangeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InputError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InvalidRomanNumeralError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def ValidationOfRomanNumerals(string):
    import re

    return bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", string))


op_roman = 1
op_arabic = 2

operation_list = ["Roman to Arabic", "Arabic to Roman"]

allowed_operations = [op_roman, op_arabic]

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
