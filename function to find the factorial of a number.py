def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)

result=factorial(5)
print(f"The Factorial=",result)
