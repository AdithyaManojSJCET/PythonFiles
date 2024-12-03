def multiply_numbers(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+multiply_numbers(num1,num2-1)

result=multiply_numbers(5,7)
print(f"The product=",result)