# Assignment 1: List Sum [Warm-up]
# Return the sum of a list without sum().

def list_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

# Example
numbers = [1, 2, 3, 4, 5]
print(list_sum(numbers))