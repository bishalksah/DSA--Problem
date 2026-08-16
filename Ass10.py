# Assignment 10: Is Prime? [Easy]
# Return True if n (>=0) is prime.
# Test divisors only up to sqrt(n).

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True 
print(is_prime(11))  # Output: True
print(is_prime(15))  # Output: False