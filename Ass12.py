# Assignment 12: Count Vowels [Easy]
# Return how many vowels (a,e,i,o,u) are in a string, case-insensitive.

def count_vowels(n):
    count = 0
    vowels="aeiou"
     
    for char in n.lower():
        if char in vowels:
            count += 1
    return count
print(count_vowels("hello bishal"))
    