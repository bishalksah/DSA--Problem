# Assignment 17: Collatz Steps [Medium]
# Count steps to reach 1: if even halve it, if odd do 3n+1.
# Example: 6 -> 8 steps

def collatz_steps(n):
    if n == 1:
        return 0
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
print(collatz_steps(6))