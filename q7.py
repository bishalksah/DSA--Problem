# Assignment 7: Set Intersection [Warm-up]
# Return the common elements of two lists (as a set).


def set_intersection(list1, list2):
    return set(list1) & set(list2)      
print(set_intersection([1, 2, 3], [2, 3, 4]))  # Output: {2, 3}
