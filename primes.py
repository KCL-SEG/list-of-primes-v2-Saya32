"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    while True:
        try:
            for i in range(2, number_of_primes + 1):
                for j in range(2, int(i ** 0.5) + 1):
                    if i%j == 0:
                        break
                    else:
                        primes.append(i)
            return list
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")