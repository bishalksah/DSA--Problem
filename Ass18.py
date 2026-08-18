# Assignment 18: Digit Sum (Digital Root) [Medium]
# Repeatedly sum the digits until one digit remains.
# Example: 9875 -> 9+8+7+5=29 -> 2+9=11 -> 2.
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n    
print(digit_sum(9875))