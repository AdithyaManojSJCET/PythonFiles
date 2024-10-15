'''
Author: Adithya Manoj
Date: 15-10-2024

Python Program to find the smallest number
'''
num1=int(input("Enter a Number: "))
num2=int(input("Enter a Number: "))
num3=int(input("Enter a Number: "))

if num1<num2 and num1<num3:
    print(num1,"is the smallest")
elif num2<num3 and num2<num1:
    print(num2,"is the smallest")
elif num3<num1 and num3<num2:
    print(num3,"is the smallest")
else:
    print("The numbers are equal")