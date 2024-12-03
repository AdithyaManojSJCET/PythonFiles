def gcd(num1, num2):
    if num1%num2==0:
        return num2
    else:
        return gcd(num1,num2&num1)

result=gcd(1220,516)
print(f"The Greatest Common Divisor is",result)