i = int(input())
x = 1
a = 0
while x<=i//2:
    if i%x ==0:
        a+=x
    x+=1
if a == i:
    print(f'{i} is a perfect number')
else:
    print(f'{i} is not a perfect number')

