'''Write a program to take an integer ranging form 0 to 6 and print corresponding weekday 
(Week starts from Monday)
input: 2
output: Wednesday'''
n = int(input())
if 0<=n<=6:
    if n == 0:
        print("Monday")
    elif n == 1:
        print("Tuesday")
    elif n == 2:
        print("Wednesday")
    elif n == 3:
        print("Thursday")
    elif n == 4:
        print("Friday")
    elif n == 5:
        print("Saturday")
    else:
        print("Sunday")
else:
    raise ValueError