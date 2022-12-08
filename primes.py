"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    # Check if argument is 0 or negative number
    if number_of_primes <= 0:
        raise ValueError("Argument must be a positive number")

    # Create an empty list to store prime numbers
    list = []

    # Set current number to 2 (first prime number)
    current_number = 2

    # Iterate until the number of prime numbers is reached
    while len(list) < number_of_primes:
        # Create a flag to indicate if current_number is prime
        is_prime = True

        # Iterate from 2 to current_number to check for divisibility
        for i in range(2, current_number):
            if current_number % i == 0:
                is_prime = False
                break

        # If number is prime, add it to the list
        if is_prime:
            list.append(current_number)

        # Increment current_number
        current_number += 1
