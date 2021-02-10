from palidrome import palindrome
from test_cases import test_cases


for txt, expectation in test_cases.items():
    assert palindrome(txt) == expectation, f"Expected {expectation!r} got {palidrome(txt)!r}"
