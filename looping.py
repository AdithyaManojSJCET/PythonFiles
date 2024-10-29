'''
Author: Adithya Manoj
Date: 29-10-2028
Programme to Check whether the given number is PRIME
'''

num=int(input("Enter a Number: "))
is_Prime=True

for i in range(2,(num//2)+1):
    if num%i==0:
        is_Prime = False
        break
if is_Prime:
    print(f"{num} is prime")
else:
    print(f"{num} is not a prime")
