def add_numbers(num1,num2):
    if num2==0:
        return num1
    else:
        return add_numbers(num1+1,num2-1)

result=add_numbers(5,7)
print(f"The sum=",result)