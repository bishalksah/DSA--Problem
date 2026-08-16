# Assignment 4: Min of Three [Warm-up]
# Return the smallest of three numbers without min()

def min_of_three(a, b, c):
    if a <= b and a <= c:
        return f"{a} is the smallest"
    elif b <= a and b <= c:
        return f"{b} is the smallest"
    else:
        return f"{c} is the smallest"