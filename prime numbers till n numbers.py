'''
Author: Adithya Manoj
Date: 29-10-2028
Programme to print the prime Numbers till n
'''

limit=int(input("Enter the Limit: "))

for num in range(2, limit + 1):

    is_prime = True
    for i in range(2, num//2 + 1):
        if num % i == 0:
            is_prime = False

    if is_prime:
        print(num, end=' ')