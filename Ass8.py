# Assignment 8: Sum 1..n [Warm-up]
# Return 1+2+...+n using the closed-form formula.
def sum_1_to_n(n):
    return n * (n + 1) // 2
print(sum_1_to_n(10))  # Output: 55