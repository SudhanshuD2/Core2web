r_c = int(input(': '))
r = r_c
while r>0:
    c = 1
    while c<=r:
        if c%2==0:
            print(0, end=' ')
        else:
            print(1, end=' ')
        c+=1
    r-=1
    print()