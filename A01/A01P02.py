'''Write a python program to check wheather the number is negative, positive or equal to zero
Input: -2
Output: -2 is the negative number'''
a = int(input())
if a>0:
    print("{} is the positive number".format(a))
elif a<0:
    print("{} is the negative number".format(a))
else:
    print("{} is zero".format(a))
