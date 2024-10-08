'''
Auther : Adithya Manoj
Date : 8-10-2024
Program to find the current date and time
Version = 1.0
'''
from datetime import datetime
current_time=datetime.now()
print(current_time)
format_1=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format_1)
format_2=current_time.strftime("%m/%d/%Y ")
print(format_2)
format_3=current_time.strftime("%a,%m,%y")
print(format_3)
format_4=current_time.strftime("%a,%m,%Y %H:%M:%S %p")
print(format_4)
format_5=current_time.strftime("%a-%b %H:%M:%S IST %Y")
print(format_5)
format_6=current_time.strftime("%a-%b %H:%M:%S IST %Y")
print(format_6)
format_7=current_time.strftime("%a")
print(format_7)
format_8=current_time.strftime("%H:%M:%S")
print(format_8)
format_9=current_time.strftime("%m")
print(format_9)
format_10=current_time.strftime("%Y")
print(format_10)