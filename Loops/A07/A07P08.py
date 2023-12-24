inp = int(input())
n = inp
pal = 0
while inp>0:
    dgt = inp%10
    pal = (pal*10)+dgt
    inp//=10
if pal == n:
    print(f'{n} is pallindrome number')
else:
    print(f'{n} is not pallindrome')
