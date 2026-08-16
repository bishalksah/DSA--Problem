# Assignment 5: Is Divisible [Warm-up]
# Return True if a is exactly divisible by b.
def is_divisible(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    elif a % b == 0:
        return True
    else:
        return False
print(is_divisible(10, 2))  # Output: True