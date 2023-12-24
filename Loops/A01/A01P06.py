'''Write a program to check wheather the character is Alphabet or not
Input: v
Output: v is an alphabet'''

a = input()

if 'a'<= a <= 'z' or 'A' <= a <= 'Z':
    print("{} is an alphabet".format(a))
else:
    print("{} is not alphabet". format(a))
