import pytest
from prime_factorisation import prime_factors


def test_prime_factors():
    assert callable(prime_factors)


def test_illegal_symbols():
    with pytest.raises(ValueError):
        prime_factors("screwdriver")


def test_num_as_prime():
    with pytest.raises(ValueError):
        prime_factors(47)