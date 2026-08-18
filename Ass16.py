# Assignment 16: Celsius→Fahrenheit Table [Medium]
# Return a list of (c, f) pairs for c from start to stop inclusive, step.
# f = c*9/5 + 32.
 
def celsius_to_fahrenheit_table(start, stop, step):
    table = []
    for c in range(start, stop + 1, step):
        f = c * 9 / 5 + 32
        table.append((c, f))
    return table
print(celsius_to_fahrenheit_table(0, 100, 20))