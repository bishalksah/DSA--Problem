# Assignment 13: Factorial (Iterative) [Easy]
# Return n! iteratively (0! = 1).

def factorial(n):
    result = 1
    for i in range( 1 ,n+1):
        result = result *i
    return result         
print(factorial(5))

