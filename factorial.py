'''
Author: Adithya Manoj
Date: 15-10-2024

Python Program to find the factorial for the number
'''
n=int(input("Enter A number: "))
f=1
while n>0:
    f=f*n
    n-=1
print(f)