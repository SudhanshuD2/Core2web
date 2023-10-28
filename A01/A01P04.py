'''Write a program to check wheather the number is divisible by 5 or not
input: 55
output: 55 is divisible by 5'''
a = int(input())
if a%5 ==0:
    print("{} is divisible by 5".format(a))
else:
    print("{} is not divisible by 5".format(a))