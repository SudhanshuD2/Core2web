i = int(input())
f_count = i
f_armstrong = i
digi_c = 0
#Digit counting
while f_count>0:
    digi_c+=1
    f_count//=10

su = 0
#Armstrong number
while f_armstrong>0:
    digi = f_armstrong%10
    su += digi**digi_c
    f_armstrong//=10

if su == i:
    print(f'{i} is Armstrong number')
else:
    print(f'{i} is not Armstrong number')
