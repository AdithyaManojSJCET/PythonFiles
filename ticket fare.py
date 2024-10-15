'''
Author: Adithya Manoj
Date: 15-10-2024

Python Program to determine the entry-ticket fare.
'''
age=int(input("Enter your age: "))
if age<10:
    print("The fare will be 7")
elif age>=10 and age<60:
    print("The Fare will be 20")
else:
    print("The Fare will be 5")