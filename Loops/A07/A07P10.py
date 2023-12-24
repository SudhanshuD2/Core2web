def factorial(i1):
    facto = 1
    while i1>0:
        facto *= i1
        i1-=1
    return facto

i = int(input())
ix = i
su = 0
while ix>0:
    digits = ix%10
    su += factorial(digits)
    ix//=10

if i == su:
    print(f'{i} is Strong number')
else:
    print(f'{i} is not a strong number')
