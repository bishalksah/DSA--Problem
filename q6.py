    # Assignment 6: Squares Comprehension [Warm-up]
    # Return squares of 0..n-1 as a list.
def squares(n):
    return [i**2 for i in range(n)]
print(squares(5))  # Output: [0, 1, 4, 9, 16]