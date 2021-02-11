from prime_factorisation import prime_factors


def test_prime_factors():
    try:
        from prime_factorisation import prime_factors

        assert callable(prime_factors), "prime_factors not callable"
    except ImportError as error:
        assert False, error


def test_num_as_prime():
    try:
        prime_factors(47)
        assert False, "ValueError expected"
    except ValueError:
        pass


def test_illegal_symbols():
    try:
        prime_factors("screwdriver")
        assert False, "ValueError expected"
    except ValueError:
        pass


if __name__ == "__main__":
    for test in (
        test_prime_factors,
        test_num_as_prime,
        test_illegal_symbols,
    ):
        print(f"{test.__name__}: ", end="")
        try:
            test()
            print("OK")
        except AssertionError as error:
            print(error)
