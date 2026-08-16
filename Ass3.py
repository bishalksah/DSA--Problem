# Assignment 3: Max of Two [Warm-up]
# Return the larger of a and b without max().
def max_of_two(a, b):
    return f"{a} is bigger than {b}" if a >= b else f"{b} is bigger than {a}"
print(max_of_two(10, 5))  # Output: 10