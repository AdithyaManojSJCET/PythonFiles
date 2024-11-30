'''
Author:Adithya Manoj
Date: 30/11/2024
Program to check whether the given number is valid or not.
'''

def valid_number():
    number=input("Enter your number: ")
    if len(number)==10 and (number[0]=='7' or number[0]=='8' or number[0]=='9') :
        print("Number is valid")
    else:
        print("The Number is Invalid!")


valid_number()
