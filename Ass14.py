# Assignment 14: Reverse Integer [Easy]
# Reverse the digits of a non-negative integer.
# Example: 1230 -> 321

def reverse_integer(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num
print(reverse_integer(1230))