i = int(input())
x = 2
a = 0
while x<=i//2:
    if i%x == 0:
        a+=1
    x+=1
if a == 0:
    print(f'{i} is not a prime number')
else:
    print(f'{i} is a prime number')
