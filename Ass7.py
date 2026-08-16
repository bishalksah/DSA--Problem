# Assignment 7: Letter Grade [Warm-up]
# Map a 0–100 score to A/B/C/Fail (>=90, >=75, >=40, else)
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "Fail"
print(letter_grade(30))  # Output: Fail