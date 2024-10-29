'''
Author: Adithya Manoj
Date: 29-10-2028
Programme to Print the multiplication table
'''

num=int(input("Enter A Number: "))

for i in range(1,12+1):
    print(f"{num} * {i}\t = {num*i}")