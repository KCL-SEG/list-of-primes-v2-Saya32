"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Number of primes should be a positive number.")

    list = []
    number = 2
    while len(list) < number_of_primes:
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
        if prime:
            list.append(number)
        number += 1
    return list