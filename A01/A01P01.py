'''Write a program to find maximum between 2 numbers
Input: 1 2
Output: 2 is Max number between 1&2'''
a = int(input())
b = int(input())
if a>b:
    print("{0} is Max number between {0}&{1}".format(a,b))
else:
    print("{1} is Max number between {0}&{1}".format(a,b))