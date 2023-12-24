'''Write a program to check wheather the input character is a vovel or consonant
input: a
output: vovel
input: b
output: consonant'''
a = input()
a = a.lower()
if 'a' <= a <= 'z':
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        print("Vovel")
    else:
        print("Consonant")
