# Assignment 5: Char Frequency [Warm-up]
# Return a dict of character counts for a string.
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
print(char_frequency("hello world"))  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}