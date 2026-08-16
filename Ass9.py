# Assignment 9: Swap Without Temp [Easy]
# Return (a, b) with their values swapped, without a temp variable.
def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return (a, b)   
print(swap_without_temp(5, 10))  # Output: (10, 5)