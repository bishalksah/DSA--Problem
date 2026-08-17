# Assignment 15: GCD (Euclid) [Easy]
# Return the greatest common divisor of a and b.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a    
print(gcd(48, 18))