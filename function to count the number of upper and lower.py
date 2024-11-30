'''
Author:Adithya Manoj
Date: 30/11/2024
Program to count the number of UPPER and LOWER characters in string
'''
def case_counter():
    upper=0
    lower=0
    sample='The quick Brow Fox'

    for i in range(0,len(sample)):
        if sample[i].isupper():
            upper+=1
        elif sample[i].islower():
            lower+=1
    return upper,lower

upper,lower=case_counter()

print("No of Upper characters: ",upper)
print("No of Lower characters: ",lower)