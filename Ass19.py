# Assignment 19: Two-Number Calculator [Stretch]
# Parse a string 'a op b' (op is + - * /) and return the result as float.
# Example: '6 / 4' -> 1.5 ; '3 * 5' -> 15.0


def two_number_calculator(expression):
    a, op, b = expression.split()
    a, b = float(a), float(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b   
print(two_number_calculator('6 / 4')) 
    