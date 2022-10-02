"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError

    for primeNumber in range(100000):
        if primeNumber > 1:
            for i in range(2, primeNumber):
                if (primeNumber % i) == 0:
                    break
            else:
                list.append(primeNumber)
                if len(list) == number_of_primes:
                    break

    return list
