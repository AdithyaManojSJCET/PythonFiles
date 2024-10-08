'''
Auther :Febin Noble
Date : 8-10-2024
Program to extract first name
Version : 1.0

'''
first_name=input("Enter your first name : ")
second_name=input("Enter your second name : ")
full_name=first_name +" " + second_name
print(full_name)
length=len(first_name)
print(length)
extracted_first_name=full_name[:length]
print(extracted_first_name)