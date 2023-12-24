i = int(input())
dgt = 0
while i>0:
    digit = i%10
    if digit%2 == 0:
        dgt+=1
    i//=10
print(dgt)