'''
Author: Adithya Manoj
Date: 15-10-2024

Python Program to check whether the given number
is postive or not
'''
number=int(input("Enter the number: "))
if number>0:
    print("The Given number",number,"is Positive")
elif number<0:
    print("The Given Number",number,"is Negative")
else:
    print("The Given number is 0")