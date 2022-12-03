"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    try:
            i = 2        # first prime number
            while len(list) != number_of_primes:    # while list is not full
                for j in range(2, i):   # check if i is prime
                    if i % j == 0:      # if i is not prime
                        break       # break the loop
                else:       # if i is prime
                    list.append(i)    # append i to list
                i+=1    # increment i
            return list     # return list of primes
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
