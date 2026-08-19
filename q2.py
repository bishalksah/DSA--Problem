# Assignment 2: List Max [Warm-up]
# Return the maximum of a non-empty list without max().

def list_max(numbers):
    max_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value    
print(list_max([1, 2, 3, 4, 5 ,6]))  # Output: 5