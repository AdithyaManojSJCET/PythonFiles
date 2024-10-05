'''
Author: Adithya Manoj
Date:05-10-2024
Python programme that uses functions from the math module to perform
the following operations on a number provided by the user
'''
import math
#Accepting the value from the user
number=int(input("Enter a Number:"))
#Square Root
root=math.sqrt(number)
#Factorial
factorial=math.factorial(number)
#Exponent
power=math.pow(number,2)

#Displaying the output
print('Square Root of',number,':',root)
print('Factorial of',number,':',factorial)
print(number,'raised to power of 2:',power)
