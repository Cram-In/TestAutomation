from functools import wraps


def validate_number(function):
    @wraps(function)
    def wrapper(num):
        if num != int:
            raise ValueError("illegal symbol")
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    factors.append(i)
                    break
            else:
                raise ValueError(num, "is a prime number")

    return wrapper


@validate_number
def prime_factors(num):
    factors = []
