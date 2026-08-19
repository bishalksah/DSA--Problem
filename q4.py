# Assignment 4: Has Duplicate [Warm-up]
# Return True if any value repeats.

def has_duplicate(lst):
    return len(lst) != len(set(lst))

print(has_duplicate([1, 2, 3, 4, 5]))  # Output: False
print(has_duplicate([1, 2, 2, 3, 4]))  # Output: True