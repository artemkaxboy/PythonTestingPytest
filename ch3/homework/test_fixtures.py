import datetime

import pytest


@pytest.fixture(scope='module')
def prime_numbers():
    print("started at " + str(datetime.datetime.now()))
    yield [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print("ended at " + str(datetime.datetime.now()))


@pytest.fixture()
def street_lights():
    return {'red': 'wait', 'yellow': 'ready', 'green': 'go'}


def test_prime_numbers_odd(prime_numbers):
    for prime in prime_numbers:
        assert prime == 2 or prime % 2 != 0


def test_prime_are_close(prime_numbers):
    for i in range(len(prime_numbers)):
        assert i < 1 or prime_numbers[i] - prime_numbers[i - 1] < prime_numbers[i]
