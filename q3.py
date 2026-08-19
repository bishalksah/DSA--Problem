# Assignment 3: Unique Count [Warm-up]
# Return the number of distinct values in a list.
 
def unique_count(lst):
    return len(set(lst))

print(unique_count([1, 2, 2, 3, 3, 3]))  # Output: 3