'''
Author: Adithya Manoj
Date: 15-10-2024

Python Program to evaluate the average height of boys and girls on N no of students
'''
n=int(input("Enter The Number of Students: "))

btotal=0
gtotal=0
tbh=0
tgh=0

for a in range(1,n):
    gender=input("Enter The Gender: ")
    if gender=='m' or gender=='M':
        bheight=float(input("Enter your height: "))
        btotal+=1
        tbh=tbh+bheight
        print("Record entered\n")
    else:
        gheight=float(input("Enter your height: "))
        gtotal+=1
        tgh=tgh+gheight
        print("Record entered\n")
avg_b_height=tbh/btotal
avg_g_height=tgh/gtotal

print("The Average Height of GIRLS is:",avg_g_height)
print("The Average Height of BOYS is:",avg_b_height)