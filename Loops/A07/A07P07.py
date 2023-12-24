inp = int(input())
rev = 0
while inp>0:
    dgt = inp%10
    rev = (rev*10)+ dgt
    inp//=10

print(rev)