'''
Author: Adithya Manoj
Date: 15-10-2024
Pyhton program to find the sum of the digits of a number
'''

num=int(input("Enter A number: "))
SUM=0
while (num>0):
    r=num%10
    num=num//10
    SUM=SUM+r
print("The sum of the digits is: ",SUM)