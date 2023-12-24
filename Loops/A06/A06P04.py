facto = 1
x = int(input())
n = x
while x>=1:
    facto*=x
    x -= 1
print('Factorial of {} is {}'.format(n, facto))