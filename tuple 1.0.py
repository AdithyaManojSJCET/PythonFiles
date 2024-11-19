from itertools import repeat

fruits=('banana','apple','cherry', 'date','mango')

print(fruits[0])
print(fruits[-1])
print(fruits[-3],'\n')


#concatination
tuple1=(1,2,3,4)
tuple2=(5,6,7,8)
numbers=tuple1+tuple2
print(numbers,'\n')

#Repitition
repeat1=numbers*3
print(repeat1,'\n')

#Membership
print('banana' in fruits)

#Slicing
colours=('red','blue','green','yellow','orange')
print(colours[0:4])
print(colours[3:5])
print(colours[2:5],'\n')

#Unpack tuples into variables
person=('Adithya',18,'Student')
name,age,profession=person

print(name)
print(age)
print(profession)