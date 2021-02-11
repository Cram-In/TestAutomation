def prime_factors(num):
    factors = []
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            raise ValueError(num, "is a prime number")
