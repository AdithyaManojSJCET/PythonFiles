'''
Author: Adithya Manoj
Date: 22/10/2024
Python program to convert temperature values back and forth between Celsius and Fahrenheit.
'''

value=int(input("Enter temperature: "))
c_or_f=input("Is this in (C)elsius or (F)ahrenheit?: ")


if c_or_f=='C' or c_or_f=='c':
    f=(9/5 * value) + 32
    print(value,'Celcius is',f,'Farhenheit')
else:
    c=5/9 *(value-32)
    print(value, ' Farhenheit is', c, 'Celcius')
