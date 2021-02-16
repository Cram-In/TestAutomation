class OutOfRangeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


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
