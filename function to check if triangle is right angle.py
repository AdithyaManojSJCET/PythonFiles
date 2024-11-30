'''
Author:Adithya Manoj
Date: 30/11/2024
Program to check whether A triangle is a right angle triangle or not
'''

def right_triangel_or_not():
    sidelst=[]
    for i in range(3):
        side=int(input("Enter the Side Length: "))
        print(side,'Has been entered')
        sidelst.append(side)

    sidelst.sort()

    if sidelst[-1]**2==sidelst[0]**2 + sidelst[1]**2:
        return True
    return False


if right_triangel_or_not():
    print("The Triangle is a Right Angle Triangle!!")
else:
    print("The Triangle is NOT a Right Angle Triangle!")