'''
Author:Adithya Manoj
Date: 19/11/2024
Program to construct a pattern of stars
'''

limit=int(input("Enter the Limit: "))

print('''\n
INCREASING HILL''')
for i in range(limit+1):
    for j in range(i):
        print('*',end=' ')
    print()

print('''\n
DECREASING HILL''')
for k in range(limit+1,0,-1):
    for l in range(k):
        print('*',end=' ')
    print()


print('''\n
HILL PATTERN''')
for m in range(1,limit+1): #rows
    for n in range(limit-m): #spacing
        print(" ",end=' ')

    for o in range(1,2*m):
        print("*",end=' ')
    print()


print('''\n
REVERSE HILL''')
for m in range(limit,0,-1): #rows
    for n in range(limit-m): #spacing
        print(" ",end=' ')

    for o in range(1,2*m):
        print("*",end=' ')
    print()

