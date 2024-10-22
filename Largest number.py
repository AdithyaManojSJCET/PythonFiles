'''
Author: Adithya Manoj
Date: 22/10/2024
Python program to find the largest of three numbers.
'''

num1=int(input("Enter A number: "))
num2=int(input("Enter A number: "))
num3=int(input("Enter A number: "))

if num1>num2 and num1>num3:
    print("The largest number is:",num1)
elif num2>num3 and num2>num1:
    print("The largest number is:",num2)
else:
    print("The largest number is:",num3)
