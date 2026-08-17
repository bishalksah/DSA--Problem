# Assignment 11: FizzBuzz [Easy]
# Return a list for 1..n: 'Fizz' (÷3), 'Buzz' (÷5), 'FizzBuzz' (÷15), else the number as str.

def Fizzbuzz(n):
    result = []
    for i in range(1, n+1):
        
        if i % 15 == 0:
            result.append("fizzbuzz")
        elif i%3 == 0:
            result.append("fizz")
        elif i%5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result      
print(Fizzbuzz(15))  
         
