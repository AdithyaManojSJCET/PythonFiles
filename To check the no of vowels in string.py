'''
Author: Adithya Manoj
Date: 29-10-2028
Programme to Check the number of vowels in a string
'''

string_input=input("Enter A String: ")

vowels="aeiouAEIOU"
vowels_count=0

for char in string_input:
    if char in vowels:
        vowels_count+=1
print("The number of vowels are:",vowels_count)